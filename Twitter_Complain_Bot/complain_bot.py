from dotenv import load_dotenv
from os import environ, getcwd
from os.path import exists
from time import sleep

#selenium dependencies 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot():

    def __init__(self) -> None:
        self.down = ""
        self.up =""
        self.driver =  Chrome()

    def get_internet_speed(self):

        #go to internet speed test webpage
        self.driver.get("https://www.speedtest.net/")

        sleep(2)

        #start Internet speed test
        GO_btn = self.driver.find_element(By.CLASS_NAME,"start-text")
        GO_btn.click()

        sleep(60)

        #Get Internet Speed Info
        Download_speed = self.driver.find_element(By.CSS_SELECTOR,"span.download-speed").text
        Upload_speed = self.driver.find_element(By.CSS_SELECTOR,"span.upload-speed").text
        ISP_Name = self.driver.find_element(By.CLASS_NAME,"js-data-sponsor").text
        ISP_accronym = self.driver.find_element(By.CLASS_NAME,"js-data-isp").text

        sleep(2)
        Dict = {}
        Dict['ISP_Name'] = ISP_Name
        Dict['Download']=Download_speed
        Dict['Upload']=Upload_speed

        #close driver
        self.driver.close()

        return Dict

    def tweet_at_provider(self, message, actual_speed):
        #get authorization credentials
        self.authentication_credentials()

        #check if internet is underperforming
        if actual_speed < self.INTERNET_IDEAL:

            message += str(self.INTERNET_IDEAL) + " Mbs down/up !!!"

            print(message)

            #log in with credentials 
            self.driver.get("https://twitter.com/i/flow/login")

            sleep(5)

            #input user credentials
            user = self.driver.find_element(By.CSS_SELECTOR,"input.r-13qz1uu")
            user.send_keys(self.TWITTER_USER)

            user.send_keys(Keys.ENTER)

            sleep(4)

            #unusal activity pop-up
            unusual_activity = self.driver.find_element(By.CSS_SELECTOR,"input.r-13qz1uu")
            unusual_activity.send_keys(self.TWITTER_HANDLE)
            unusual_activity.send_keys(Keys.ENTER)

            sleep(4)

            #input password credentials 
            password = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password.send_keys(self.TWITTER_PASSWORD)

            password.send_keys(Keys.ENTER)  

            sleep(8)     

            #write out new tweet 

            #send tweeet 

            #close driver
            self.driver.close()



        else:
            print("Internet Speed not slow enough to complain! ")

    def authentication_credentials(self):

        #build environment path
        env_path = f"{getcwd()}\secrets.env"

        if exists(env_path):
            #load environemnt path 
            load_dotenv(env_path)

            #get twitter credentials for login
            self.TWITTER_USER = environ.get("TWITTER_USER")
            self.TWITTER_PASSWORD = environ.get("TWITTER_PASSWORD")
            self.TWITTER_HANDLE = environ.get("TWITTER_HANDLE")
            self.INTERNET_IDEAL = int(environ.get("INTERNET_IDEAL"))

        else:
            #incorrect execution path
            print("Incorrect execution path or secrets.env file missing! ")
            print(env_path)