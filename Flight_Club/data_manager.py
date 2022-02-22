import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,api_end_point):
        self.end_point = api_end_point
    def update_iata(self,data):
        for row in data:
            info = {"price": row}
            response = requests.put(url=f"{self.end_point}/{row['id']}",json=info)
    def get_info(self):
        #connect to google sheet and get price info 
        response = requests.get(url=self.end_point)
        response.raise_for_status()
        #list of flight dictionaries
        self.flight_data = response.json()['prices']
        return self.flight_data