
#environment dependencies 
from os import getcwd, environ
from os.path import exists
from dotenv import load_dotenv

#beautiful soup dependencies 
import requests
from bs4 import BeautifulSoup
import pprint


#selenium dependencies 
from selenium.webdriver import Chrome


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

    
    def scrape_zillow_bs4(self):
        #using beautiful soup scrape data and store temporarily 

        #build endpoint url 
        endpoint = f"https://www.zillow.com/homes/{self.CITY},-{self.STATE}_rb/"

        page = requests.get(url=endpoint)

        soup = BeautifulSoup(page.content, "html.parser")
        pprint.pprint(soup.contents)

        for ul_elem in soup.find_all("ul", {'class': "List-c11n-8-73-8__sc-1smrmqp-0 srp__sc-1psn8tk-0 bfcHMx photo-cards"}):
            for li_elem in ul_elem.find_all('li'):
                print(li_elem.text)


    def push_to_google_form():
        #using selenium automate the filling out of forms using scraped data
        #https://forms.gle/ezHsJmEvu2eTzbbo9
        pass