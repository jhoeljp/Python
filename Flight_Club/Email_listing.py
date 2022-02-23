import requests
import smtplib as mail

class Users:
  def __init__(self):
    self.users_end_point = "your_user_google_sheet_end_point"
    self.get()
  def get(self):
    response = requests.put(url=self.users_end_point)
    response.raise_for_status()
    self.users_sheet_body = response.json()
    self.data = response.json()['users']
  def post(self,new_user):
    # self.users_sheet_body.append(news_user)
    response = requests.post(url=self.users_end_point,body=new_user)
    response.raise_for_status()
    response.text()
    print("Sucessfully added to Flight Club email list! ")
  def user_exists(self,user_dict):
    for row in self.data:
      #compare if email already on sheet
      if self.data["Email"] == user_dict["Email"]:
        return "You are already in the club!"
    #if user's email not in list post email with info 
    #Add to Google Sheet with user list
    self.post(user_dict)
  def send_email(email,password,email_receiver):
    with mail.SMTP("stmp.gmail.com") as connection:
      connection.starttls()
      connection.login(user=email,password=password)
      message = f"Subject:Welcome to Flight Club!\nCongrats, you will receive flight deals once a week!"
      connection.send_message(msg=message, from_addr=email, to_addrs=email_receiver)
    print("Registration Sucessful, check your email :D")

def type_email(email_1,email_2):
  loop = False
  while not loop:
    email_1 = input("What is your email ?: ").lower()
    email_2 = input("Type your again email ?: ").lower()
    loop = email_1 == email_2
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