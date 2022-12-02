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
        self.driver.maximize_window()

        sleep(3)

        #input login credentials 
        insta_user = self.driver.find_element(By.NAME,"username")
        insta_user.send_keys(self.USER)

        insta_password = self.driver.find_element(By.NAME,"password")
        insta_password.send_keys(self.PASSWORD)

        #send login in credentials
        insta_password.send_keys(Keys.ENTER)

        sleep(7)
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

        sleep(6)
        
        #go to the followers section
        page = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a")
        page.click()

        sleep(4)
        #locate body of pop-up page
        follower_body = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")

        #scroll continously or for a set range
        #scroll 25 times with 8 accounta a page
        scroll = 0

        while scroll < 100:

            #scroll down every 5 seconds 
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', follower_body)
            
            sleep(5)
            scroll += 1

        #terminate selenium driver 
        self.driver.close()

        self.driver.quit()

    def follow(self):
        pass
