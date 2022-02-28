# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
RED = "#e7305b"

#font
FONT = ("Arial",50,"bold")
LETTER_FONT = ("Arial",20,"normal")

#dependencies
from Timer import Timer
from tkinter import Canvas,PhotoImage,Label,Button,Tk

# ---------------------------- UI SETUP ------------------------------- #

#Setup main window
window = Tk()
window.title("Pomodoro GUI")
print(window.winfo_rgb(color=RED))
window.config(padx=100,pady=50,bg=YELLOW)

#Tomato canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text="00:00",font=FONT)
canvas.grid(column=1,row=1)

#GUI Title 
main_title = Label(text="Timer",bg=YELLOW,fg=RED,highlightthickness=0,font=FONT)
main_title.grid(column=1,row=0)

#Check Mark Displayer  
mark = "✔"
check_mark = Label(text="",bg=YELLOW,fg=RED,highlightthickness=0)
check_mark.grid(column=1,row=3)


# ---------------------------- TIMER  ------------------------------- # 
#Timer Class 
timer = Timer(window=window,title=main_title,canvas=canvas,timer_text=timer_text,check_mark=check_mark)

# ---------------------------- TIMER  ------------------------------- # 


#Start Timer Button
start_b = Button(text="Start",bg=YELLOW,highlightthickness=0,highlightbackground=YELLOW
                ,command= timer.start_timer)
start_b.grid(column=0,row=2)

#Reset Timer Button 
reset_b = Button(text="Reset",bg=YELLOW,highlightthickness=0,highlightbackground=YELLOW
                ,command= timer.reset_timer)
reset_b.grid(column=2,row=2)

#START 
window.mainloop()