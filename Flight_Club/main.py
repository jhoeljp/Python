#DEPENDENCIES
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
from os import getcwd, environ

#ENVIRONMENT VARIABLES
ENV_FILE = "secrets.env"

#Load Environment file 
full_path = f"{getcwd()}/{ENV_FILE}"
load_dotenv(full_path)

#Variables
GOOGLE_SHEET_PRICE = environ.get("SHEETY_API_END_POINT_PRICES")
FLIGHTS_API_KEY = environ.get("TEQUILA_API_END_POINT")
EMAIL_SENDER = environ.get("EMAIL_SENDER")
EMAIL_RECEIVER = environ.get("EMAIL_RECEIVER")
PASSWORD = environ.get("PASSWORD")
EMAIL_SERVER = environ.get("EMAIL_SERVER")

#Sheety API Class
dt = DataManager(GOOGLE_SHEET_PRICE)

#GET Google Sheet info 
sheet_data = dt.get_info()

#Tequila by Kiwi.com API Class
flight = FlightSearch(FLIGHTS_API_KEY)

# UPDATE sheet's IATA codes if empty 
for row in sheet_data:
    if row['iataCode']=="":
        row['iataCode']=flight.IATA_code(row['city'])
dt.update_iata(sheet_data)

#SEARCH for cheap flights for eahc city on Google Sheetfi
DESTINATION_IATA = "DMM"
Flights = []
for row in sheet_data:
    #find cheapest flight for 
    try:
        cheapest = flight.get_cheap_flights(DESTINATION_IATA,row['iataCode'])

    #Not valid flight search request 
    except Exception:
        print(f"Could not find a valid flight from {DESTINATION_IATA} to {row['city']}")

    #Valid flight has been found 
    else:

        #dont display non existent flights 
        if cheapest['arrivalCity'] != "":
            Flights.append(cheapest)
            

# Sent Email of cheap flights 
notify_obj = NotificationManager(Flights,EMAIL_SENDER,EMAIL_RECEIVER,PASSWORD,EMAIL_SERVER)
# notify_obj.send_email()