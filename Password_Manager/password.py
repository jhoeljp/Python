from string import ascii_lowercase, ascii_uppercase
from random import choice, shuffle, randint
from tkinter import END, Entry, messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class Password_Manager():
    def __init__(self,input_bar, file):

        #Password File local
        self.PASSWORD_FILE = file

        #Dictionary of Entries from tkinter 
        self.input_bar = input_bar

        #Password constants
        self.letters_lower = list(ascii_lowercase)
        self.letters_upper = list(ascii_uppercase)
        self.numbers = [str(i) for i in range(0,10)]
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_password(self):

        password_list = ""

        #random amount of input types
        password_list += "".join(choice(self.letters_lower) for _ in range(randint(1, 3)))
        password_list += "".join(choice(self.letters_upper) for _ in range(randint(2, 3)))
        password_list += "".join(choice(self.symbols) for _ in range(randint(2, 4)))
        password_list += "".join(choice(self.numbers) for _ in range(randint(2, 4)))

        #shuffle eandom characters
        password_list = list(password_list)
        shuffle(password_list)
        password_list = ''.join(password_list)

        #paste password on entry box and copy to clipboard
        self.input_bar["Password"].delete(0,END)
        self.input_bar["Password"].insert(0,password_list)


    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def try_save_info(self,new_data,website):
        with open(self.PASSWORD_FILE,"r") as file:
            #load old data
            json_obj = json.load(file)

            #load up new data
            json_obj[website] = new_data[website]

        with open(self.PASSWORD_FILE,"w") as file:
            #save new data
            #wipe out clear Website and password
            json.dump(json_obj,file,indent=4)
            

    def try_fetch_info(self,website):
        #load old data
        with open(self.PASSWORD_FILE,"r") as file:
            json_obj = json.load(file)

            #fetch match for website
            #raises exception is match doesnt exist 
            return json_obj[website]


    #Saves user's input in local file
    def save_info(self):

        #obtain input entries from the entrys' dictionary 
        tmp = [self.input_bar[i].get() for i,v in self.input_bar.items()]
        line = ",".join(tmp) + "\n"

        #pop-up confirmation 
        website = self.input_bar["Website"].get().lower()
        email = self.input_bar["Email/Username"].get()
        password = self.input_bar["Password"].get()

        #create new entry 
        new_data = {
            website:{
            "Email/Username":email,
            "Password":password
            }   
        }

        #show warning message 
        if website== "" or password=="" or email=="":
            messagebox.showinfo(title="Oops",message="Oops!\n\nDon't leave any fields empty...")
        else:
            #write new line to save file 
            try:
                self.try_save_info(new_data,website)
            
            except FileNotFoundError as e:
                #create blank json file
                with open(self.PASSWORD_FILE,"w") as file:
                    file.write("{}")

                #try again with new file 
                self.try_save_info(new_data,website)

            #delete user entries for fresh re-start
            finally:
                self.input_bar["Website"].delete(0,END)
                self.input_bar["Password"].delete(0,END)

    
    #Search button for locally saved passowrds
    def fetch_password(self):
        website = self.input_bar["Website"].get().lower()

        if website == "":
            messagebox.showinfo("Invalid website.")
        else:
            #fetch json file for website password 
            try:
                data = self.try_fetch_info(website)
            
            #avoid error of unexistant file
            except FileNotFoundError as e:
                messagebox.showinfo(title="FileNotFoundError", message="Oops nothing to see, File is empty.")

            #catch exception is match doesnt exist as well
            except KeyError as e:
                messagebox.showinfo(title = "KeyError",message=f"Oops {website} password is not stored.")
            else:
                #must have match to execute without exception 
                email = data["Email/Username"]
                password =  data["Password"]

                #display saved data to user 
                messagebox.showinfo(title="Success",message=f"Email: {email}\nPassword:{password}")