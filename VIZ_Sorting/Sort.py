'''
Name: Jhoel Perez 
Date: Feb 16, 2022
Purpose: 
Implement Merge Sort, Heap Sort, Quick Sort, Bubble Sort.
Make sorting processes visible as well.
'''
from tkinter import *
RED = "#EA5455"
BAR_COLOR = "#F07B3F"
BACKGROUND = "#A8D8EA"
GREEN = "#65C18C"

class Sorting():
    def __init__(self) -> None:
        pass
    def paint_green(self):
        #paint existing rectangles green  
        self.active_canvas.itemconfig(self.left_rect, fill=GREEN)
        self.active_canvas.itemconfig(self.right_rect, fill=GREEN)
    def paint_red(self):
        print("paiting red")
        #paint existing rectangles green  
        self.active_canvas.itemconfig(self.left_rect, fill=RED)
        self.active_canvas.itemconfig(self.right_rect, fill=RED)
    def paint_normal(self):
        #paint existing rectangles back to nornaml  
        self.active_canvas.itemconfig(self.left_rect, fill=BAR_COLOR)
        self.active_canvas.itemconfig(self.right_rect, fill=BAR_COLOR)

    def bubble_sort(self,array_dict,active_canvas:Canvas,active_window:Tk):
        self.active_canvas = active_canvas
        self.active_window = active_window
        # for i in array_dict: print(i)
        #obtain array with lengths to bubble sort 
        #'y_length' is the magnitude of the bar
        arr = [rectangle['y1'] for rectangle in array_dict]
        #'rectangle' is the canvas rectangle we created 
        bar_arr = [rectangle['id'] for rectangle in array_dict]

        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                #rectangles lengths or magnitude
                left = arr[j]
                right = arr[j+1]
                #rectangles ids
                self.left_rect = bar_arr[j]
                self.right_rect = bar_arr[j+1]
                #change color to red to display comparison is underway
                # self.active_window.after(0,self.paint_red)
                # active_window.after(500,self.change_color)
                #Bubble Up!
                if left > right:
                    #paint existing rectangles green  
                    #wait period to display switch is on the way
                    # active_window.after(2000,self.paint_green)

                    #move rectangle by difference of x coodinates
                    distance = array_dict[j+1]['x0']-array_dict[j]['x0']
                    #move left rectangle to right 
                    active_canvas.move(self.left_rect,(distance),0)
                    #move right rectangle to left 
                    active_canvas.move(self.right_rect,(-distance),0)
                    #update dict list of active rectangles (for coordinate re-drawing on x-axis)
                    bar_arr[j], bar_arr[j+1] = bar_arr[j+1], bar_arr[j] 
                    #update list for making comparison
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                #wait to display movement to user 
                #paint them to their orignal color 
                # active_window.after(2000,self.paint_normal)