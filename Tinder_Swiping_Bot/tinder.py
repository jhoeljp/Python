from dotenv import load_dotenv
from os import getcwd
from os.path import exists
from os import environ
from time import sleep

#selenium dependencies 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

env_path = f"{getcwd()}\secrets.env"

if exists(env_path):
    
    #Load environment variables 
    load_dotenv(env_path)

    Tinder_USER = environ.get("USER")
    Tinder_PASSWORD = environ.get("PASSWORD")

    #navigate to login page with selenium 
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.tinder.com")

    sleep(2)
    #accept all browser cookies 
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]").click()

    sleep(2)
    #click to log in with environ variables
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]").click()

    sleep(2)
    #login with facebook 
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]").click()

    sleep(3)
    #input login credentials on pop-up
    email = driver.find_element(By.ID,"email")
    email.send_keys(Tinder_USER)

    password = driver.find_element(By.ID,"pass")
    password.send_keys(Tinder_PASSWORD)

    #login
    password.send_keys(Keys.ENTER)


    sleep(500)

    driver.close()
    driver.quit()


else:
    print("Incorrect execution path or file 'secrets.env' missing! ")
    print(env_path)