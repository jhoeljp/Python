import requests
import smtplib as mail

class Users:
  def __init__(self):
    self.users_end_point = "your_user_google_sheet_link"
    self.get()

  #fetch user details from google sheet 
  def get(self):

    #make request 
    response = requests.get(url=self.users_end_point)

    #raise error on request if any 
    response.raise_for_status()

    #unwrap data from put response 
    self.users_sheet_body = response.json()
    self.data = response.json()['users']


  #edit sheet with new user information 
  def post(self,new_user):
    #send info with new user
    response = requests.post(url=self.users_end_point,body=new_user)
    response.raise_for_status()
  
  #Find if users is in Newslettter already
  def user_exists(self,user_dict):
    for _ in self.data:

      #compare if email already on sheet
      if self.data["Email"] == user_dict["Email"]:
        return "You are already in the club!"
    
    #if user's email not in list post email with info 
    #Add to Google Sheet with user list
    self.post(user_dict)

  #Send email confirmation verifying succesful registration 
  def send_email(email,password,email_receiver):

    #connect to server 
    with mail.SMTP("stmp.gmail.com") as connection:
      connection.starttls()

      #login with internal email details 
      connection.login(user=email,password=password)
      message = f"Subject:Welcome to Flight Club!\nCongrats, you will receive flight deals once a week!"
      
      #send email message 
      connection.send_message(msg=message, from_addr=email, to_addrs=email_receiver)


def type_email(email_1,email_2):

  loop = False

  #Keep asking until users does not fail verification
  while not loop:
    email_1 = input("What is your email ?: ").lower()
    email_2 = input("Type your again email ?: ").lower()

    loop = email_1 == email_2

    #Verification has failed 
    if not loop: 
      print("Email entries do not match! try again ...")
  
  return email_1

#WELCOME
print("Welcome to Jhoel's Flight Club! ")
print("We find the best flight deals and email you.")

#USER INFO
info = {}
info["First_name"] = input("What is your first name: ").title()
info["Last_name"] = input("What is your last name: ").title()
info["Email"]= type_email("1","2")

#SHEETY API
user_obj = Users()
user_obj.user_exists(info)