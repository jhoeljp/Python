'''
Date:12/03/2022

Scrape renting data from zillow.com 

Congragate all info as structured data on Google Sheet

https://forms.gle/ezHsJmEvu2eTzbbo9

'''

from renting_deals import Rent_Deals


if __name__ == "__main__":

    try:
        #init class
        bot = Rent_Deals()

        #scrape zillow for info
        bot.scrape_zillow_bs4()

        #input all data on google sheet 
        bot.push_to_google_form()

    except Exception as ex:
        print(str(ex))