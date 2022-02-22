import smtplib as mail
'''
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
'''
class NotificationManager:
    #Send Emai notification with price list
    def __init__(self,flights,email_sender,email_reciever,password,email_server):
        self.email_server = email_server
        self.email_sender = email_sender
        self.email_reciever = email_reciever
        self.password = password
        self.list_of_flights = flights
        self.msg_subject = "Cheap Flights Alert !!!"
        self.create_message()
    #Creates complete string message to be sent on email
    def create_message(self):
        self.final_msg = "Low price alert!\n\n"
        for cheap_flight in self.list_of_flights:
            price = cheap_flight["lowest_price"]
            departure = f"{cheap_flight['departureCity']}-{cheap_flight['departureIATA']}"
            destination = f"{cheap_flight['arrivalCity']}-{cheap_flight['arrivalIATA']}"
            outbound_date = cheap_flight["outboundDate"]
            inbound_date = cheap_flight["inboundDate"]
            self.final_msg += f"Only ${price} to fly from {departure} to {destination}, from {outbound_date} to {inbound_date}. \n"
        print(self.final_msg)
    def send_email(self):
        with mail.SMTP(self.email_server) as connection:
            connection.starttls()
            connection.login(user=self.email_sender,password=self.password)
            connection.sendmail(from_addr=self.email_sender,
                                to_addrs=self.email_reciever,
                                msg=f"Subject:{self.msg_subject}\n{self.final_msg}")
        print(f"EMAIL SENT TO : {self.email_reciever}")