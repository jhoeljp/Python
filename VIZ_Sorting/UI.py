#Name: Jhoel Perez #Date: Feb 17, 2022
#Dependencies 
from tkinter import *
from random import choice 
#Color palette hexs
BLUE = "#A8D8EA"
PURPLE = "#AA96DA"
PINK = "#FCBAD3"
YELLOW = "#FFFFD2"
GREEN = "#65C18C"
FONT = ("Courier",20,"normal")

class GUI():
    def __init__(self) -> None:
        #define window
        self.window = Tk()
        self.window.title("Sorting Algortihtms VIZ")
        self.window.minsize(height=500,width=800)
        self.window.config(bg=BLUE,padx=30,pady=30)
        #make top bar 
        self.make_button_bars()
        #make canvas to display array to sort 
        self.make_canvas()
        #test
        self.test_draw_array()
        self.window.mainloop()
    def test_draw_array(self):
        #test draw array 
        arr = [choice(range(30,300)) for i in range(32)]
        self.draw_array(arr)
    def make_canvas(self):
        self.canvas = Canvas(height=400,width=800,background="white")
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0,row=1,columnspan=7,pady=40)
    def draw_array(self,array):
        #width of bar will depend on how many bar are being displayed 
        #width of rectangle
        # x_width = 100/len(array)
        x_width = 15
        #initial drawing coordinates
        x_0,y_0,x_1,y_1 = 0,0,0,0
        padx = 10
        for length in array:
            #height of the rectangle
            y_length = length
            x_1 = x_1+x_width+padx
            # y_1 = y_length
            self.canvas.create_rectangle(x_0, y_0, x_1, y_length, fill=choice(["#2D4059","#EA5455","#F07B3F","#FFD460"]))
            #move drawing origin point of rectangle
            x_0 = x_0+x_width+padx
    def make_button_bars(self):
        #gui has four sections 
        #1) create array button 
        self.create_array = Button(text="Create New Array ")
        self.create_array.grid(row=0,column=0)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)
        #2) change array size (and sorting speed) 
        self.scale_min = 4
        self.scale_max = 200
        self.slide_bar = Scale(self.window, from_=self.scale_min, to=self.scale_max, orient=HORIZONTAL)
        self.slide_bar.grid(row=0,column=1)
        self.slide_bar.config(bg=BLUE,highlightbackground=BLUE)
        #3) button bar with sorting algorithms 
        # Merge Sort, Heap Sort, Quick Sort, Bubble Sort
        #automize this in the future 
        self.create_array = Button(text="Merge Sort")
        self.create_array.grid(row=0,column=2)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)

        self.create_array = Button(text="Heap Sort")
        self.create_array.grid(row=0,column=3)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)

        self.create_array = Button(text="Quick Sort")
        self.create_array.grid(row=0,column=4)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)

        self.create_array = Button(text="Bubble Sort")
        self.create_array.grid(row=0,column=5)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)
        #4) Sort button to start vizualization and sorting 
        self.create_array = Button(text="Sort!")
        self.create_array.grid(row=0,column=6)
        self.create_array.config(bg=BLUE,highlightbackground=BLUE,padx=20,pady=20,font=FONT)