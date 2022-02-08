
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20

COUNT = 10
REPS = 0

from math import floor
from tabnanny import check
from tkinter import *
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    #work 25 > 5 min brake (4 times)
    #20 min brake 
    #change title accordingly
    print(REPS)
    #if last rep 8th cycle 
    if REPS==7:
        main_title.config(text="Long Brake",fg=GREEN)
        count_down(LONG_BREAK_MIN*60)
    #work 25
    elif REPS%2==0:
        main_title.config(text="Work Time",fg=RED)
        count_down(WORK_MIN*60)
    else:
        #five minute brake
        main_title.config(text="Short Brake",fg=GREEN)
        count_down(SHORT_BREAK_MIN*60)
    REPS+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count >= 0:
        min = floor(count/60)
        seconds = count%60 if (count%60)>9 else f"0{count%60}"
        canvas.itemconfig(timer_text,text=f"{min}:{seconds}")
        window.after(1000,count_down,count-1)
    else:
        if REPS%2 != 0: 
            tmp_mark = str(check_mark.cget("text")) + mark
            check_mark.config(text = tmp_mark)
        if REPS<8:
            start_timer()
# ---------------------------- UI SETUP ------------------------------- #
FONT = ("Arial",50,"bold")
LETTER_FONT = ("Arial",20,"normal")

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
check_mark = Label(text="",bg=YELLOW,fg=RED,highlightthickness=0)
check_mark.grid(column=1,row=3)

window.mainloop()