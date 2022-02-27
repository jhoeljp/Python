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

        #email login info 
        self.email_server = email_server
        self.email_sender = email_sender
        self.email_reciever = email_reciever
        self.password = password

        #message info to be sent 
        self.list_of_flights = flights
        self.msg_subject = "Cheap Flights Alert !!!"

        #send email message 
        self.create_message()
    
    #Creates complete string message to be sent on email
    def create_message(self):
        #message headline 
        self.final_msg = "Low price alert!\n\n"

        #make a line for each deal found 
        for cheap_flight in self.list_of_flights:

            #unwrap info from cheap_flight dict in a readable format
            price = cheap_flight["lowest_price"]
            departure = f"{cheap_flight['departureCity']}-{cheap_flight['departureIATA']}"
            destination = f"{cheap_flight['arrivalCity']}-{cheap_flight['arrivalIATA']}"
            outbound_date = cheap_flight["outboundDate"]
            inbound_date = cheap_flight["inboundDate"]

            #build deal sentence 
            self.final_msg += f"Only ${price} to fly from {departure} to {destination}, from {outbound_date} to {inbound_date}. \n"

    #Send email wiht user details provided
    def send_email(self):

        #establish server connection 
        with mail.SMTP(self.email_server) as connection:
            connection.starttls()

            #login with user secrets 
            connection.login(user=self.email_sender,password=self.password)

            #send mail with constructed message string 
            connection.sendmail(from_addr=self.email_sender,
                                to_addrs=self.email_reciever,
                                msg=f"Subject:{self.msg_subject}\n{self.final_msg}")