from selenium import webdriver
from time import sleep
from dotenv import load_dotenv
from os import getcwd, path, environ
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#load account details for login 
environment_file = f"{getcwd()}\secrets.env"

if not path.exists(environment_file):
    print("secrets.env file does not exist, or incorrect execution path. ")
    print(environment_file)
else:
    #get account details 
    load_dotenv(environment_file)

    USER = environ.get("EMAIL")
    PASSWORD = environ.get("PASSWORD")
    LOCATION = environ.get("LOCATION")

    #got to job posting url 
    jobs_url ="https://www.linkedin.com/"

    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(jobs_url)

    #log in into Linkedin account 
    user_element = driver.find_element(By.ID, "session_key")
    user_element.send_keys(USER)

    password_element = driver.find_element(By.ID, "session_password")
    password_element.send_keys(PASSWORD)

    sigin_button = driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
    sigin_button.click()

    sleep(3)

    #easy apply job postings 
    job_search_link = "https://www.linkedin.com/jobs/search/?currentJobId=3368389848&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CP%2CC%2CT%2CI&f_WT=1%2C2%2C3&geoId=102890719&keywords=data%20analyst&location={LOCATION}&refresh=true&sortBy=R"
    driver.get(job_search_link)

    job_listing_elem = driver.find_elements(By.CLASS_NAME, "scaffold-layout__list-container")

    sleep(3)

    job_list = job_listing_elem[0].find_elements(By.TAG_NAME,"li")

    #apply for each position available 
    for i in job_list:

        actions = ActionChains(driver)

        #click of job posting to open application 
        actions.move_to_element(i)
        actions.click()
        actions.perform()

        sleep(1)

        print(i.text)

        #get a hold of easy apply button 

    sleep(500)
    

    driver.close()
    driver.quit()