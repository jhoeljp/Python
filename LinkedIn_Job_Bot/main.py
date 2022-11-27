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
    
    sleep(2)

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

    sleep(2)

    #bypass security check
    try:
        signin_2_btn = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
        signin_2_btn.click()

        sleep(1.4)

        #log in into Linkedin account 
        user_element = driver.find_element(By.NAME, "session_key")
        user_element.send_keys(USER)

        password_element = driver.find_element(By.NAME, "session_password")
        password_element.send_keys(PASSWORD)

        # sigin_button = driver.find_element(By.CLASS_NAME,"btn__primary--large from__button--floating")
        # sigin_button.click()
        sleep(1)
        password_element.send_keys(Keys.ENTER)

    except Exception as ex:
        print(str(ex))
        pass

    sleep(500)
    #container of job postings
    job_listing_elem = driver.find_elements(By.CLASS_NAME, "scaffold-layout__list-container")
    
    #list of all job postings
    job_list = job_listing_elem[0].find_elements(By.TAG_NAME,"li")

    #each position available 
    for job in job_list:

        actions = ActionChains(driver)

        #click of job posting 
        actions.move_to_element(job)
        actions.click()
        actions.perform()

        sleep(1.2)

        try:

            #apply for each position available 
            #click on the easy apply button 
            # driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button").click()
            driver.find_element(By.CLASS_NAME,"jobs-apply-button--top-card").click()

            #using available resume on LinkedIn
            #asuming all input data is already available 
            #click next until reaching end of application
            sleep(1.5)

            #2 STEP APPLICATIONS ONLY
            #if longer it get ignored

            #initial info form
            next_btn = None
            try:
                next_btn = driver.find_element(By.CLASS_NAME,"artdeco-button__text")
            except:
                print("failed to find button 1")
            
            try:
                next_btn = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button/span")
            except:
                print("failed to find button 2")

            #email/ phone code/ and phone application
            try:
                next_btn = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
            except:
                print("failed to find button 3")
                                                     
            next_btn.click()
            sleep(1)

            #either review of next buttons
            next_btn = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
            next_btn.click()

            #logner than 3 step, presses discart changes to continue parsing
            sleep(1)
            next_btn = driver.find_element(By.CLASS_NAME,"artdeco-button__text")
            next_btn.click()

            #submit application button
            sleep(1)
            submit_btn = driver.find_element(By.CLASS_NAME,"artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
            submit_btn.click()


            sleep(500)

        except Exception as ex:
            # print(str(ex))
            #if not complete in 4 ignore posting on go to the next
            pass

        sleep(2)

    driver.close()
    driver.quit()