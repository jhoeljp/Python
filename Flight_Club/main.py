#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

flight = FlightSearch()

#GET Google Sheet info 
dt = DataManager()
sheet_data = dt.get_info()

# UPDATE sheet's IATA codes if empty 
for row in sheet_data:
    if row['iataCode']=="":
        row['iataCode']=flight.IATA_code(row['city'])
dt.update_iata(sheet_data)
DESTINATION_IATA = "CCS"
#SEARCH for cheap flights for eahc city on Google Sheetfi
for row in sheet_data:
    cheapest = flight.get_cheap_flights(DESTINATION_IATA,row['iataCode'])
    price = cheapest["lowest_price"]
    from_city = row['city']
    bags = cheapest["bag_price"]
    print(f"{from_city} for {price} | luggage: {bags} ")
    print(cheapest["link"])
    print("-----------------------------------")