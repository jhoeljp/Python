from dotenv import load_dotenv
from os import getcwd
from os.path import exists
from os import environ

env_path = f"{getcwd()}\secrets.env"

if exists(env_path):
    
    #Load environment variables 
    load_dotenv(env_path)

    Tinder_USER = environ.get("USER")
    Tinder_PASSWORD = environ.get("PASSWORD")

    print(f"{Tinder_USER} with @{Tinder_PASSWORD}")

else:
    print("Incorrect execution path or file 'secrets.env' missing! ")
    print(env_path)