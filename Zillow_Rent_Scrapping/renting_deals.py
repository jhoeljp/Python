
#environment dependencies 
from os import getcwd, environ
from os.path import exists
from dotenv import load_dotenv
from time import sleep

#beautiful soup dependencies 
import requests
from bs4 import BeautifulSoup
import pprint
import re
import json
import pandas as pd
import lxml
import csv


#selenium dependencies 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class Rent_Deals():

    def __init__(self) -> None:
        #initialize selenium driver
        # self.driver = Chrome()

        #load search criteria
        self.get_search_criteria()


    def get_search_criteria(self) -> None:
        #load environment path
        env_path = f"{getcwd()}\secrets.env"

        if exists(env_path):
            
            #load environment variables
            load_dotenv(env_path)

            #sotre environment variables on secret file 
            self.CITY = environ.get("CITY")
            self.STATE = environ.get("STATE")
            self.PRICE_PER_MONTH = environ.get("PRICE_PER_MONTH")

        #invalid exewcution path 
        else:
            print("Invalid execution path or secrets.env missing !!! ")
            print(env_path)

    def scrape_zillow(self):

        self.driver = Chrome()

        #build endpoint url 
        endpoint = f"https://www.zillow.com/homes/{self.CITY},-{self.STATE}_rb/"

        self.driver.get(endpoint)

        sleep(5)
        

        apartments_grid = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div/div/div[1]/ul")

        #scroll down 5 times to load all page 
        for i in range(5):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', apartments_grid)
            sleep(5)

        for li_elem in apartments_grid.find_elements(By.CSS_SELECTOR,"li"):
            print(li_elem.text)


        sleep(500)
        self.driver.close()
        self.driver.quit()


    def scrape_zillow_bs4(self):
        #using beautiful soup scrape data and store temporarily 

        #build endpoint url 
        endpoint = f"https://www.zillow.com/homes/{self.CITY},-{self.STATE}_rb/"

        #heading params for request
        #add headers in case you use chromedriver (captchas are no fun);

        params = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
        }

        # data1 = ""
        # with requests.Session() as s:
        #     r1 = s.get(endpoint, headers=params)

        #     # data1 = json.loads(re.search(r'!--(\{"queryState".*?)-->', r1.text).group(1))

        #     data1 = r1
        #     pprint.pprint(r1.text)

        #     print("-------------------------------------")

        print(endpoint)

        page = requests.get(url=endpoint,headers=params)

        soup = BeautifulSoup(page.content, "html.parser")

        #get list of zillow elements
        Zillow =[]

        for ul_elem in soup.select("ul.List-c11n-8-73-8__sc-1smrmqp-0.srp__sc-1psn8tk-0.bfcHMx.photo-cards.with_constellation"):
            for li_elem in ul_elem.find_all('li'):
                Zillow.append(li_elem.text)

        self.Rent_info = {
        'address':[],
        'price':[],
        'link':[]
        }
        #do some data manipulation and store on dictionary
        for l in Zillow:

            try:
                #get true price of rent
                house = l.split('$')
                price = str(house[1]).split(' ')[0]

                #get address of residence
                info = house[0].split(',')
                address = info[0]
                city = info[1]

                # TX 77091RE/MAX PREMIER
                zip_code = info[2][4:9]

                print(f"{address} on {city} at zip {zip_code} for the price of {price}")

                #append to dictionary 
                self.Rent_info['address'].append(f"{address},{city},{zip_code}")
                self.Rent_info['price'].append(price)

                #find property link
                self.Rent_info['link'].append("N/a")


            except Exception as ex:
                # print(str(ex))
                pass


    def push_to_google_form(self):
        #using selenium automate the filling out of forms using scraped data
        #https://forms.gle/ezHsJmEvu2eTzbbo9

        try:
            #initialize seleniu driver 
            self.driver = Chrome()

            #link to google form 
            google_endpoint = "https://forms.gle/ezHsJmEvu2eTzbbo9"

            for index in range(0,len(self.Rent_info['address'])):
                print(f"index: {index}")
                sleep(5)

                #make url request to google form
                self.driver.get(google_endpoint)

                sleep(6)

                #locate input boxes on google form 
                form = self.driver.find_elements(By.CSS_SELECTOR,"div.Qr7Oae")
                print(f"form inputs: {len(form)}")

                sleep(1)

                #locate address input box 
                address_input = form[0].find_element(By.CSS_SELECTOR,"input.whsOnd.zHQkBf")

                # #locate price input box 
                price_input = form[1].find_element(By.CSS_SELECTOR,"input.whsOnd.zHQkBf")

                # #locate link input box 
                link_input = form[2].find_element(By.CSS_SELECTOR,"input.whsOnd.zHQkBf")

                # for property in self.Rent_info:
                address_input.send_keys(self.Rent_info['address'][index])
                price_input.send_keys(self.Rent_info['price'][index])
                link_input.send_keys(self.Rent_info['link'][index])

                sleep(3)
                #click submit button 
                submit_btn = self.driver.find_element(By.CSS_SELECTOR,"span.snByac")
                submit_btn.click()

            # else:
            #     print('Google form elements could not be found !!!')
            #     print(len(form))
        except Exception as ex:
            print(str(ex))

        #close selenium driver
        self.driver.close()
        self.driver.quit()
