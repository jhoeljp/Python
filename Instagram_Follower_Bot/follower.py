#dependencies
from time import sleep 
from dotenv import load_dotenv
from os import getcwd, environ
from os.path import exists
from sys import exit

#selenium dependencies 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Instagram_Follower():
    def __init__(self) -> None:
        self.driver = Chrome()
        self.URL = "https://www.instagram.com/"

    def login(self):

        #get authorization credentials 
        self.authentication_credentials()

        #login on instagram 
        self.driver.get(self.URL)

        sleep(3)

        #input login credentials 
        insta_user = self.driver.find_element(By.NAME,"username")
        insta_user.send_keys(self.USER)

        insta_password = self.driver.find_element(By.NAME,"password")
        insta_password.send_keys(self.PASSWORD)

        #send login in credentials
        insta_password.send_keys(Keys.ENTER)

        sleep(4)
        # sleep(400)
        #dismiss notification pop-up 
        self.driver.find_element(By.CSS_SELECTOR,"button._a9_1").click()

        sleep(4)

        
    def authentication_credentials(self):

        env_path = f"{getcwd()}\secrets.env"

        if exists(env_path):

            #load environment file path 
            load_dotenv(env_path)

            #assign environment variables 
            self.USER = environ.get("USER")
            self.PASSWORD = environ.get("PASSWORD")
            self.TARGET_ACCOUNT = environ.get("TARGET_ACCOUNT")

        else: 
            #invalid 
            print("Invalid execution path or secrets.env file missing !!!")
            print(env_path)
            exit()


    def find_followers(self):
        #got to target account 
        self.driver.get(self.URL+'/' + self.TARGET_ACCOUNT)

        sleep(4)
        

        sleep(400)
        pass
    def follow(self):
        pass
