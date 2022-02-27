#Kiwi Tequila Flight Search API 
import requests 
from datetime import datetime
from dateutil import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,api_key) -> None:
        self.end_point = "https://tequila-api.kiwi.com"

        #TEQUILA API Key 
        self.api_key = api_key
        self.header = {"apikey":self.api_key}


    def get_cheap_flights(self,departure_code,destination_code):

        #Search end point
        end_point = f"{self.end_point}/v2/search"

        #6 month date difference in the dd/mm/YYYY format 
        tomorrow = datetime.now() + relativedelta.relativedelta(days=1)
        self.start_date = (tomorrow).strftime("%d/%m/%Y")
        self.end_date =  (tomorrow + relativedelta.relativedelta(months=6)).strftime("%d/%m/%Y")

        #round trips that return from 7 to 28 days from departure date 
        return_from = (tomorrow + relativedelta.relativedelta(days=7)).strftime("%d/%m/%Y")
        return_to = (tomorrow + relativedelta.relativedelta(days=28)).strftime("%d/%m/%Y")

        #currency
        currency = "USD"

        #body parameters of search 
        parameters ={
            "fly_from":departure_code,
            "fly_to":destination_code,
            "date_from":self.start_date,
            "date_to":self.end_date,
            "flight_type":"round",
            "return_from":return_from,
            "return_to":return_to,
            "curr":currency
        }

        #request info 
        response = requests.get(url=end_point,headers=self.header,params=parameters)
        response.raise_for_status()

        #unpack response from server if request was valid 
        data = response.json()

        #find the cheapest flight of them all 
        #add parameter stop_overs=1 
        cheapest_flight = {
            "lowest_price":1000,
            "departureCity":"",
            "departureIATA":"",
            "arrivalCity":"",
            "arrivalIATA":"",
            "outboundDate":"",
            "inboundDate":"",
            "link":"",
            "bag_price":0
        }

        #populate info to display it on email message 
        for i in data['data']:

            #get current flight price 
            price = i['conversion'][currency]

            #Get the cheapest flight available
            if cheapest_flight["lowest_price"] > price: 

                #price info
                cheapest_flight["lowest_price"]=price

                #departure info
                cheapest_flight["departureCity"]=i['cityFrom']
                cheapest_flight["departureIATA"]=i['cityCodeFrom']

                #arrival info 
                cheapest_flight["arrivalCity"]=i['cityTo']
                cheapest_flight["arrivalIATA"]=i['cityCodeTo']

                #ROUND TRIP outbound and inbound dates (%Y-%m-%d)
                cheapest_flight["outboundDate"]=((i['route'])[0])['local_departure'].split("T")[0]
                cheapest_flight["inboundDate"]=((i['route'])[len(i['route'])-1])['local_arrival'].split("T")[0]

                #extra info
                cheapest_flight["link"]=i['deep_link']
                cheapest_flight["bag_price"]=i['bags_price']

        return cheapest_flight

    #obtain iata code of city from api
    #iata its a required parameter on search request
    def IATA_code(self,city):
        end_point = f"{self.end_point}/locations/query"
        query = {"term": city, "location_types": "city"}

        #make request
        response = requests.get(url=end_point,headers=self.header,params=query)
        response.raise_for_status()

        #get iata code from response
        return (response.json()['locations'][0])['code']