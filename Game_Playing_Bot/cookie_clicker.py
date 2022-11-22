from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from random import randint

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By

#open cookie clicker game on browser
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#find cookie and click continously 
cookie = driver.find_element(By.ID,"cookie")

#find store elements by id
store = driver.find_elements(By.ID,"store")
store_items = store[0].text.split("\n")

#build dictionary as upgrade catalog with price
Upgrades = {}

for item in store_items[::2]:

    item,price = item.split(" - ")

    #build id tag 
    category = f"buy{item}"

    Upgrades[category]=int(price.replace(',',''))

#start timer 
start = time.time()

while True:
    #click on cookie for currency
    cookie.click()

    #buy upgrades every 5 minutes
    if time.time()-start >= randint(5,30):

        #current currency balance 
        money = driver.find_element(By.ID,"money").text
        money = int(money.replace(',',''))

        #what is most expensive upgrade we can afford
        top_value = 0
        upgrade_id = ""

        for key,val in Upgrades.items():

            if val > top_value and money >=val:
                upgrade_id = key
                top_value = val

        #located and buy upgrade
        driver.find_element(By.ID,upgrade_id).click()
        print(f"bought {upgrade_id} for {top_value}")
        
        #reset timer 
        start = time.time()




# driver.close()