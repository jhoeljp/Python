#DEPENDENCIES
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json
import string

#GLOBAL variables
BG = "#FFEDD3"
FONT_COLOR = "#FC4F4F"
BAR_COLOR = "#FE8F8F"
EMAIL = "default@gmail.com"
PASSWORD = "12345"
PASSWORD_FILE = "passwords.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#password constants
letters = list(string.ascii_letters)
numbers = [str(i) for i in range(0,10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = ""
    #random amount of input types
    #select number of randoms
    password_list += "".join(choice(letters) for _ in range(randint(3, 5)))
    password_list += "".join(choice(symbols) for _ in range(randint(2, 4)))
    password_list += "".join(choice(numbers) for _ in range(randint(2, 4)))

    #shuffle eandom characters
    password_list = list(password_list)
    shuffle(password_list)
    password_list = ''.join(password_list)

    #paste password on entry box and copy to clipboard
    input_bar["Password"].delete(0,END)
    input_bar["Password"].insert(0,password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def try_save_info(new_data,website):
    with open(PASSWORD_FILE,"r") as file:
        #load old data
        json_obj = json.load(file)

        #load up new data
        json_obj[website] = new_data[website]

    with open(PASSWORD_FILE,"w") as file:
        #save new data
        #wipe out clear Website and password
        json.dump(json_obj,file,indent=4)
            

def try_fetch_info(website):
    #load old data
    with open(PASSWORD_FILE,"r") as file:
        json_obj = json.load(file)

        #fetch match for website
        #raises exception is match doesnt exist 
        return json_obj[website]


def save_info():
    global input_bar

    #obtain input entries from the entrys' dictionary 
    tmp = [input_bar[i].get() for i,v in input_bar.items()]
    line = ",".join(tmp) + "\n"

    #pop-up confirmation 
    website =input_bar["Website"].get().lower()
    email = input_bar["Email/Username"].get()
    password = input_bar["Password"].get()
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
            try_save_info(new_data,website)
        
        except FileNotFoundError as e:
            #create blank json file
            with open(PASSWORD_FILE,"w") as file:
                file.write("{}")

            #try again with new file 
            try_save_info(new_data,website)

        #delete user entries for fresh re-start
        finally:
            input_bar["Website"].delete(0,END)
            input_bar["Password"].delete(0,END)

def fetch_password():
    global input_bar
    website =input_bar["Website"].get().lower()

    if website == "":
        messagebox.showinfo("Invalid website.")
    else:
        #fetch json file for website password 
        try:
            data = try_fetch_info(website)
        
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

# ---------------------------- UI SETUP FUNCTIONS ------------------------------- #

#create text labels for gui at position on grid = acc
def create_labels(text_labels,acc):
    for i,_ in text_labels.items():
        tmp_label = Label(text=i,font=("Courier",20,"bold"),bg=BG,fg=FONT_COLOR,justify=CENTER)
        tmp_label.config(padx=0,pady=15)
        tmp_label.grid(column=0,row=acc)
        acc+=1
        text_labels[i] = tmp_label
    return text_labels

def create_bars(input_bar,acc):
    #acc+1(0) is starting row on grid
    bar_widths_list = [19,36,19]
    for i,_ in input_bar.items():
        tmp_bar = Entry(text=i)
        tmp_bar.config(width=bar_widths_list[acc],bg=BAR_COLOR,fg="#000000")

        #expand the bar to 2 columns
        if bar_widths_list[acc] > max(bar_widths_list)-1:
            tmp_bar.grid(column=1,row=acc+1,columnspan=2)
        #especific layout requirement
        else: 
            tmp_bar.grid(column=1,row=acc+1)
        acc+=1
        input_bar[i] = tmp_bar
    return input_bar

# ---------------------------- UI SETUP ------------------------------- #

#setup GUI window
window = Tk()
window.title("PassWord Manager")
window.minsize(width=200,height=200)
window.config(padx=30,pady=30,bg=BG)

#declare picture canvas
canvas = Canvas(window,width=200,height=200,highlightthickness=0,bg=BG)
logo_img = PhotoImage(file='logo.png')
logo_img_canvas = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#text labels #ROW 0
text_labels = {"Website":"",
            "Email/Username":"","Password":""}
text_labels = create_labels(text_labels=text_labels,acc=1)

#text inputs
input_bar = {"Website":"",
            "Email/Username":"","Password":""}
input_bar = create_bars(input_bar=input_bar,acc=0)

#Search password button 
Search_bt = Button(text="Search")
Search_bt.config(bg=BAR_COLOR,highlightbackground=BG,command=fetch_password)
Search_bt.grid(column=2,row=1)

#Add Buttom
Add_bt = Button(text="Add")
Add_bt.config(width=35,bg=BAR_COLOR,highlightbackground=BG,command=save_info)
Add_bt.grid(column=1,row=4,columnspan=2)

#Generate password button 
Gen_pass_bt = Button(text="Generate password")
Gen_pass_bt.config(bg=BAR_COLOR,highlightbackground=BG,command=generate_password)
Gen_pass_bt.grid(column=2,row=3)

#Main loop text labels
input_bar["Website"].focus()
input_bar["Email/Username"].insert(0,EMAIL)
input_bar["Password"].insert(0,PASSWORD)

#Main loop start
window.mainloop()