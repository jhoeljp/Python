'''
Name: Jhoel Perez 
Date: 11/15/2022
Objective: 

Track object prices and send email when price changes 
I need some headphones so I will track this headset 

https://www.amazon.sa/-/en/HyperX-HHSS1C-BA-BK-Cloud-Stinger-Core/dp/B08634653D/ref=sr_1_3?crid=HUJ6UKDWOJ7P&keywords=Gaming+Headset+for+PC&qid=1668536900&qu=eyJxc2MiOiIxLjk0IiwicXNhIjoiMS4yNSIsInFzcCI6IjAuMDAifQ%3D%3D&refinements=p_n_feature_twelve_browse-bin%3A27957730031%2Cp_n_feature_eight_browse-bin%3A27315962031&rnid=27315961031&s=videogames&sprefix=gaming+headset+for+pc%2Caps%2C189&sr=1-3

'''

from requests import get
from bs4 import BeautifulSoup as bsoup
import smtplib
from dotenv import load_dotenv
from os import getcwd, environ
import ssl

#get environment path 
env_path = f"{getcwd()}\secrets.env"
print(env_path)

load_dotenv(env_path)

#load email variables for smtp 
EMAIL_USER = environ.get("EMAIL")
PASSWORD = environ.get("PASSWORD")
EMAIL_SERVER = environ.get("EMAIL_SERVER")


#amazon link to track
end_point = "https://www.amazon.sa/-/en/HyperX-HHSS1C-BA-BK-Cloud-Stinger-Core/dp/B08634653D/ref=sr_1_3?crid=HUJ6UKDWOJ7P&keywords=Gaming+Headset+for+PC&qid=1668536900&qu=eyJxc2MiOiIxLjk0IiwicXNhIjoiMS4yNSIsInFzcCI6IjAuMDAifQ%3D%3D&refinements=p_n_feature_twelve_browse-bin%3A27957730031%2Cp_n_feature_eight_browse-bin%3A27315962031&rnid=27315961031&s=videogames&sprefix=gaming+headset+for+pc%2Caps%2C189&sr=1-3"

#heading params for request
params = {
"Accept-Language":"en-US,en;q=0.5",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
}

#get lxml parse of web page 
html = get(url=end_point,headers=params)
soup = bsoup(html.text,"lxml")

#find price by class
price = soup.find("span", {"class": "a-offscreen"})

#extract true price as float number 
amz_price = float(''.join([i for i in price.get_text() if i.isnumeric() or i=='.']))

#send email alert when price drops from original 
good_price = 400

if amz_price <= good_price:
    ssl_port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(EMAIL_SERVER,ssl_port,context=context) as connection:
        try:     
            #login with internal email details 
            connection.login(user=EMAIL_USER,password=PASSWORD)
            
            message = """
                    Subject: Amazon Alert!

                    Go buy some new headsets, the price has dropped to about 300 SAR.
                    
                    https://www.amazon.sa/-/en/HyperX-HHSS1C-BA-BK-Cloud-Stinger-Core/dp/B08634653D/ref=sr_1_3?crid=HUJ6UKDWOJ7P&keywords=Gaming+Headset+for+PC&qid=1668536900&qu=eyJxc2MiOiIxLjk0IiwicXNhIjoiMS4yNSIsInFzcCI6IjAuMDAifQ%3D%3D&refinements=p_n_feature_twelve_browse-bin%3A27957730031%2Cp_n_feature_eight_browse-bin%3A27315962031&rnid=27315961031&s=videogames&sprefix=gaming+headset+for+pc%2Caps%2C189&sr=1-3
                    
                    """
            
            #send email message 
            connection.sendmail(msg=message, from_addr=EMAIL_USER, to_addrs=EMAIL_USER)
            
        except smtplib.SMTPException as e :
            print("Email could not be sent! ")
            print(e)
        finally: 
            connection.quit()
else:
    print(f"price is still greater than {good_price}")