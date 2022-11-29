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

    #store main window handle as master 
    master_handle = driver.window_handles[0]

    sleep(3)
    #accept all browser cookies 
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]").click()

    sleep(3)
    #click to log in with environ variables
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]").click()

    sleep(3)
    #login with facebook 
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]").click()

    sleep(3)
    #get hold of popup window handle and switch driver 
    popup_handle = driver.window_handles[1]
    driver.switch_to.window(popup_handle)

    #input login credentials on pop-up
    email = driver.find_element(By.ID,"email")
    email.send_keys(Tinder_USER)

    password = driver.find_element(By.ID,"pass")
    password.send_keys(Tinder_PASSWORD)

    #login
    password.send_keys(Keys.ENTER)

    sleep(5)
    #switch back to main browser window 
    driver.switch_to.window(master_handle)
    
    #allow browser to get location
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]").click()

    sleep(2)
    #click not interest about getting new matches notification 
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[2]").click()

    #reject dark mode for browser 
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[2]/button").click()

    sleep(2)
    #send unlimited likes 
    #maximum set of likes for non premium users is 100
    like_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button")

    sleep(500)

    for i in range(100): 
        
        like_btn.click()
        sleep(2)


        #detect when its a match
        try:
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button").click()
        except Exception as ex:
            print("Profile is not a match!")

        sleep(0.5)

    driver.close()
    driver.quit()


else:
    print("Incorrect execution path or file 'secrets.env' missing! ")
    print(env_path)