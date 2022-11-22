from selenium import webdriver
from os import getcwd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver = f'{getcwd()}\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")

print(article_count.text)

driver.close()
driver.quit()