#Dependencies
from tkinter import *
from math import floor

#GUI Color Palette
RED = "#e7305b"
GREEN = "#9bdeac"

#Time Constants
WORK_MIN = 40
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#Timer Tracker
TIMER = None
COUNT = 10
REPS = 0

class Timer:
    def __init__(self,window,title,canvas,timer_text,check_mark) -> None:
        #Passover GUI Tkinter elements
        self.window = window
        self.main_title = title
        self.canvas = canvas 
        self.timer_text = timer_text
        self.check_mark = check_mark
        
    # ---------------------------- TIMER RESET ------------------------------- # 
    def reset_timer(self):
        global REPS
        REPS=0
        self.window.after_cancel(TIMER)
        self.main_title.config(text = "Timer",fg=RED)
        self.canvas.itemconfig(self.timer_text,text="00:00")

    # ---------------------------- TIMER MECHANISM ------------------------------- # 
    def start_timer(self):
        global REPS
        #work 25 > 5 min brake (4 times)
        #20 min brake 
        #change title accordingly

        #if last rep 8th cycle 
        if REPS==7:
            self.main_title.config(text="Brake",fg=GREEN)
            self.count_down(LONG_BREAK_MIN*60)

        #work 40 min
        elif REPS%2==0:
            self.main_title.config(text="Work",fg=RED)
            self.count_down(WORK_MIN*60)

        #five minute brake
        else:
            self.main_title.config(text="Brake",fg=GREEN)
            self.count_down(SHORT_BREAK_MIN*60)

        #keep track of how many reps 
        REPS+=1

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    def count_down(self,count):
        if count >= 0:
            global TIMER
            #Minutes
            min = floor(count/60)

            #Seconds
            seconds = count%60 if (count%60)>9 else f"0{count%60}"

            #Update Time being displayed 
            self.canvas.itemconfig(self.timer_text,text=f"{min}:{seconds}")

            #update timer displayed after 1 second
            TIMER = self.window.after(1000,self.count_down,count-1)

        else:
            #After each Work session dislpay a check mark tracker 
            if REPS%2 != 0: 
                tmp_mark = str(self.check_mark.cget("text")) + "✔"
                self.check_mark.config(text = tmp_mark)
            
            #keep calling timer as long as Study session is in progress
            if REPS<8:
                self.start_timer()
            
            #8 time sessions have been complete, end program
            else:
                self.main_title.config(text="Pomodoro Complete ",fg=GREEN)