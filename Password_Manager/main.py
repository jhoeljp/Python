#DEPENDENCIES
from tkinter import *
#OOP Password Manager
from password import Password_Manager

#GLOBAL variables
BG = "#FFEDD3"
FONT_COLOR = "#FC4F4F"
BAR_COLOR = "#FE8F8F"
EMAIL = "default@gmail.com"
PASSWORD = "12345"
PASSWORD_FILE = "passwords.json"

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

#setup GUI main window
window = Tk()
window.title("PassWord Manager")
window.minsize(width=200,height=200)
window.config(padx=30,pady=30,bg=BG)

#declare picture canvas for logo
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


#Password Manager Class 
password_obj =  Password_Manager(input_bar,file=PASSWORD_FILE)


#Search password button 
Search_bt = Button(text="Search")
Search_bt.config(bg=BAR_COLOR,highlightbackground=BG,command= password_obj.fetch_password)
Search_bt.grid(column=2,row=1)

#Add Buttom
Add_bt = Button(text="Add")
Add_bt.config(width=35,bg=BAR_COLOR,highlightbackground=BG,command= password_obj.save_info)
Add_bt.grid(column=1,row=4,columnspan=2)

#Generate password button 
Gen_pass_bt = Button(text="Generate password")
Gen_pass_bt.config(bg=BAR_COLOR,highlightbackground=BG,command= password_obj.generate_password)
Gen_pass_bt.grid(column=2,row=3)

#Main loop text labels
input_bar["Website"].focus()
input_bar["Email/Username"].insert(0,EMAIL)
input_bar["Password"].insert(0,PASSWORD)

#Main loop start
window.mainloop()