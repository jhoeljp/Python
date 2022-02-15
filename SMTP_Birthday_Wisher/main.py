#dependencies 
import datetime as dt
import pandas as pd 
from random import randint
import smtplib as mail
#functions 
def birthday_letter(name):
    #pick a random letter from letter templates
    rand = randint(1,3)
    FILE_LETTER = f"./letter_templates/letter_{rand}.txt"
    #replace the [NAME] with the person's actual name from birthdays.csv
    with open(FILE_LETTER) as file:
        letter = file.readlines()
    #first line replacement 
    line = letter[0].split(" ")
    # line[1]= person.name
    line[1]= name
    letter[0] = ' '.join(line)
    #get rid of list format
    return "".join(letter)
def send_email(birthday_email,letter):
    my_email = "dummy@gmail.com"
    my_password = "12345"
    email_provider = "smtp.gmail.com"
    subject_line = "Happy Birthday"
    with mail.SMTP(email_provider) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_email,msg=f"Subject:{subject_line}\n\n{letter}")
# 1. Update the birthdays.csv
FILE = "birthdays.csv"
data = pd.read_csv(FILE)
data = pd.DataFrame(data)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
# print(f"day:{day} month:{month}")
person = data[(data.day == day) & (data.month == month)]
if not person.empty:
    #pick random letter 
    arr = person.values[0]
    name, email= arr[0],arr[1]
    letter_new = birthday_letter(name)
    # 4. Send the letter generated in step 3 to that person's email address.
    send_email(email,letter_new)