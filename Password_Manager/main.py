#dependencies
from tkinter import *
from tkinter import messagebox
import random
#global variables
BG = "#FFEDD3"
FONT_COLOR = "#FC4F4F"
BAR_COLOR = "#FE8F8F"
EMAIL = "default@gmail.com"
PASSWORD = "12345"
PASSWORD_FILE = "passwords.csv"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#password constants
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = ""
    #random amount of input types
    nr_letters = random.randint(3, 5)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    #select number of randoms
    password_list += "".join(random.choice(letters) for char in range(nr_letters))
    password_list += "".join(random.choice(symbols) for char in range(nr_symbols))
    password_list += "".join(random.choice( numbers) for char in range(nr_numbers))
    #shuffle eandom characters
    password_list = list(password_list)
    random.shuffle(password_list)
    password_list = ''.join(password_list)
    # print(f"Your password is: {password_list}")

    #paste password on entry box and copy to clipboard
    input_bar["Password"].delete(0,END)
    input_bar["Password"].insert(0,password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    global input_bar
    #obtain input entries from the entrys' dictionary 
    tmp = [input_bar[i].get() for i,v in input_bar.items()]
    line = ",".join(tmp) + "\n"
    #pop-up confirmation 
    website =input_bar["Website"].get()
    email = input_bar["Email/Username"].get()
    password = input_bar["Password"].get()
    #show warning message 
    if website== "" or password=="" or email=="":
        messagebox.showinfo(title="Oops",message="Oops!\n\nDon't leave any fields empty...")
    else:
        is_ok_flag = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword:{password}\nIs it OK to save?")
        if is_ok_flag:
            #write new line to save file 
            with open(PASSWORD_FILE,"a") as file:
                file.write(line)
            #wipe out clear Website and password
            input_bar["Website"].delete(0,END)
            input_bar["Password"].delete(0,END)

# ---------------------------- UI SETUP FUNCTIONS ------------------------------- #

def create_labels(text_labels,acc):
    for i,_ in text_labels.items():
        tmp_label = Label(text=i,font=("Courier",20,"bold"),bg=BG,fg=FONT_COLOR,)
        tmp_label.config(padx=10,pady=20)
        tmp_label.grid(column=0,row=acc)
        acc+=1
        text_labels[i] = tmp_label
    return text_labels

def create_bars(input_bar,acc):
    #acc+1(0) is starting row on grid
    bar_widths_list = [35,35,21]
    for i,_ in input_bar.items():
        tmp_bar = Entry(text=i)
        tmp_bar.config(width=bar_widths_list[acc],bg=BAR_COLOR,fg="#000000")
        #expand the bar to 2 columns
        if bar_widths_list[acc] > min(bar_widths_list):
            tmp_bar.grid(column=1,row=acc+1,columnspan=2)
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
window.config(padx=50,pady=50,bg=BG)
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
#Add Buttom
Add_bt = Button(text="Add")
Add_bt.config(width=35,bg=BAR_COLOR,highlightbackground=BG,command=save_info)
Add_bt.grid(column=1,row=4,columnspan=2)
#Generate password button 
Gen_pass_bt = Button(text="Generate password")
Gen_pass_bt.config(bg=BAR_COLOR,highlightbackground=BG,command=generate_password)
Gen_pass_bt.grid(column=2,row=3)

#Main loop 
input_bar["Website"].focus()
input_bar["Email/Username"].insert(0,EMAIL)
input_bar["Password"].insert(0,PASSWORD)

window.mainloop()