
#environment dependencies 
from os import getcwd
from os.path import exists

#selenium dependencies 
from selenium.webdriver import Chrome


class Rent_Deals():

    def __init__(self) -> None:
        self.driver = Chrome()

    def get_search_criteria(self):
        #load environment path

        #load environment variables

        pass
    
    def scrape_zillow():
        #using beautiful zoup scrape data and store temporarily 
        pass

    def push_to_google_form():
        #using selenium automate the filling out of forms using scraped data
        #https://forms.gle/ezHsJmEvu2eTzbbo9
        pass