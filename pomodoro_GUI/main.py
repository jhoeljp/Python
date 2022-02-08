
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

from math import floor
from tkinter import *
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(COUNT*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = floor(count/60)
    seconds = count%60 if (count%60)>9 else f"0{count%60}"
    canvas.itemconfig(timer_text,text=f"{min}:{seconds}")
    window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #
FONT = ("Arial",50,"bold")
LETTER_FONT = ("Arial",20,"normal")
COUNT = 10

window = Tk()
window.title("Pomodoro GUI")
print(window.winfo_rgb(color=RED))
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text="00:00",font=FONT)
canvas.grid(column=1,row=1)
#Title 
main_title = Label(text="Timer",bg=YELLOW,fg=RED,highlightthickness=0,font=FONT)
main_title.grid(column=1,row=0)
#Start Button
start_b = Button(text="Start",bg=YELLOW,highlightthickness=0,highlightbackground=YELLOW,command=start_timer)
start_b.grid(column=0,row=2)
#Reset Button 
reset_b = Button(text="Reset",bg=YELLOW,highlightthickness=0,highlightbackground=YELLOW)
reset_b.grid(column=2,row=2)
#check mark 
mark = "✔"
check_mark = Label(text=f"{mark}",bg=YELLOW,fg=RED,highlightthickness=0)
check_mark.grid(column=1,row=3)

window.mainloop()