'''
Author: Jhoel Perez
Date: 5/18/2022

Input: xml file with columns of product
Ooutput: xml file with specifications of purchase of inputed product

Process ---
1) Read xml file as csv for easy parsing and search
2) put csv info on a pandas Data Frame
3) use data fram elemtents to make the search through web request
4) use selinium to click on amazon links toward products with specifications
5) Beautiful to scrape the html and xml based on identifiers like
    Name
    Dimensions: Width and Height


Requirements --
pandas
selenium

'''
import pandas as pd
from selenium import webdriver
from os import getcwd
from time import sleep
from selenium.webdriver.common.by import By


#read file for product name and specifications
excel_file = ".\\Input.xlsx"
data = pd.read_excel(excel_file)

def make_url(item):
    tmp = ''
    for i in range(len(item)):
        if item[i] == ",":
            tmp += "%2C"
        elif item[i] == " ":
            tmp += '+'
        else:
            tmp += item[i]

    return tmp

#MS Edge driver executable path
path = getcwd() + "\\msedgedriver.exe"

#open browser instance
driver = webdriver.Edge(executable_path=path)
driver.maximize_window()

try:

    for product in data["Items"]:

        #make online search for product
        search = ""
        search = make_url(product)
        print("$$$$$$$$$$$$ " + search)
        # break
        url = "https://www.google.com/search?q=" + search
        driver.get(url)
        driver.implicitly_wait(5)

        #deprecated
        # page = driver.find_element_by_link_text(item[0])

        #find element by partial text
        # pages = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=product.split(',')[0])
        lnks = driver.find_elements_by_tag_name("a")

        for i in lnks:
            print(i.get_attribute("href"))
        len(lnks)

        #click on 2 page available
        # print(len(pages))
        # if len(pages) == 1:
        #     pages[0].click()
        # if len(pages) > 1:
        #     pages[len(pages)-(len(pages)-1)].click()

        # page.screenshot_as_png()
        # page.click()
        sleep(1000)

except RuntimeError:
    print(" ################# An Exception has occurred! ")
finally:
    driver.quit()

# from bs4 import BeautifulSoup as bs

# for product in data["Items"]:
#     # print(product.split(',')[0])
#     item = product.split(',')[0]

#     #make online search for product
#     search_words = '+'.join(item.split(' '))
#     print(search_words)

#     url = "https://www.google.com/search?q=" + search_words

#     print(url)

#     page = requests.get(url)

#     soup = bs(page.content, "html.parser")

#     print(soup.find("a"))

#     break
