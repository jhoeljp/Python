from dotenv import load_dotenv
from os import environ, getcwd
from os.path import exists
from time import sleep

#selenium dependencies 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot():

    def __init__(self) -> None:
        self.down = ""
        self.up =""
        self.driver =  Chrome()

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        sleep(2)

        GO_btn = self.driver.find_element(By.CLASS_NAME,"start-text")
        GO_btn.click()

        # ISP_name = self.driver.find_element(By.CLASS_NAME,"hostUrl")
        # print(ISP_name.text)

        sleep(60)

        Download_speed = self.driver.find_element(By.CSS_SELECTOR,"span.download-speed").text
        Upload_speed = self.driver.find_element(By.CSS_SELECTOR,"span.upload-speed").text
        ISP_Name = self.driver.find_element(By.CLASS_NAME,"js-data-sponsor").text

        sleep(2)
        print(ISP_Name)
        print(f"Download Speed:{Download_speed}\nUpload Speed:{Upload_speed}")

    def tweet_at_provider():
        pass

    def authentication_credentials(self):

        env_path = f"{getcwd()}\secrets.env"

        if exists(env_path):
            load_dotenv(env_path)

            self.TWITTER_USER = environ.get("TWITTER_USER")
            self.TWITTER_PASSWORD = environ.get("TWITTER_PASSWORD")
            self.INTERNET_IDEAL = int(environ.get("INTERNET_IDEAL"))

        else:
            print("Incorrect execution path or secrets.env file missing! ")
            print(env_path)