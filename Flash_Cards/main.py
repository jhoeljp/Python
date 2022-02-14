#GLOBAL VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel",40,"italic")
WORD_FONT = ("Ariel",40,"bold")
WORDS_FILE = "./data/Study_words.csv"
SAVE_FILE = "./data/words_to_learn.csv"
TIMER = None 
CACHE = []
CACHE_unknown = []
CARD_TIME = 4000
word = ""
#DEPENDENCIES 
from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice
import os
#FUNCTIONALITY
def load_dictionary():
    #open SAVE_FILE with unknown words 
    if os.path.exists(os.getcwd() + SAVE_FILE[1:]):
        #check if file path exist and not empty
        if os.path.getsize(SAVE_FILE) !=0:
            with open(SAVE_FILE) as file:
                data = file.readlines()
                #create dictionary in set format 
            data = [line[:-1].split(',') for line in data]
            #[['histoire', 'history'], ['partie', 'par']]
            data = {w[0]: {'English': w[1]} for w in data}
            return data
    #read WORDS_FILE of SAVE_FILE is empty or undefined 
    elif os.path.exists(os.getcwd() + WORDS_FILE[1:]):
        with open(WORDS_FILE) as file:
            #primary key is french word
            data = pd.read_csv(file,index_col='French')
        # 'vieux': {'English': 'old'}
        return pd.DataFrame.to_dict(data,orient='index')
    #show error message for undefined file paths
    else:
        messagebox.showinfo(title="File not found",message=f"Invalid Vocab files:\n{WORDS_FILE}\n{SAVE_FILE}\n")
def to_learn():
    if CACHE_unknown != []:
        not_learned = [ "%s,%s\n"%(i,Dict[i]["English"]) for i in CACHE_unknown]
        with open(SAVE_FILE,"w") as file:
            file.writelines(not_learned)
        print(f"update {not_learned}")
    else:
        print("not updated CACHE_unknown is empty")
def generate_new_word():
    #no more word to study #end study session 
    if len(CACHE) == len(Study_words):
        messagebox.showinfo(message="Not more words to study",title="GOOD JOB!")
    else:
        #always generate french word
        word = choice(Study_words)
        while word in CACHE:
            #grab random word from dict not used before 
            word = choice(Study_words)
        if word!= "": CACHE.append(word)
        return word
def en_translation():
    #key word should be in foreign language 
    key = Word.cget("text")
    # print("Word to translate %s"%(key))
    return Dict[key]["English"]
def flip_to_front():
    global TIMER, word
    TIMER = window.after_cancel(TIMER)
    #get random new word not studied yet 
    word = generate_new_word()
    #change flash card looks back to normal 
    canvas.itemconfig(canvas_img, image=card_front_img)
    #change background color and flashcard contents 
    #replace title accordingly 
    Title.config(text="French",bg='white',fg='black')
    Word.config(text=word ,bg='white',fg='black')
    #flip to back of card
    TIMER = window.after(CARD_TIME,flip_to_back)
def flip_to_front_remove():
    #addd unknown word to CACHE_unknown
    if word!="": CACHE_unknown.append(word)
    #update learning to do
    to_learn()
    #pull out new flash card 
    flip_to_front()
def flip_to_back():
    #display meaning of word 
    meaning = en_translation()
    #switch image of flash card 
    canvas.itemconfig(canvas_img, image=card_back_img)
    #change text contents of flashcards and color of background and letters
    Title.config(text="English",bg=BACKGROUND_COLOR,fg='white')
    Word.config(text=meaning, bg=BACKGROUND_COLOR,fg='white')
#GUI
window = Tk()
window.minsize(height=400,width=400)
window.title("Flash Card UI")
window.config(padx=50,pady=50)
window.configure(bg = BACKGROUND_COLOR)

#Flash card 
canvas = Canvas(height=550,width=850)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(440,280,image=card_front_img)

canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)
#right button 
right_img = PhotoImage(file="./images/right.png")
button_r = Button(image=right_img)
button_r.config(bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=flip_to_front)
button_r.grid(column=1,row=1)
#wrong button 
wrong_img = PhotoImage(file="./images/wrong.png")
button_w = Button(image=wrong_img)
button_w.config(bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=flip_to_front_remove)
button_w.grid(column=0,row=1)
#title
Title = Label(window,text="",font=TITLE_FONT,bg='white',fg='black')
Title.place(x=370,y =150)
#word
Word = Label(window,text="",font=WORD_FONT,bg='white',fg='black')
Word.place(x=370,y =263)

Dict = load_dictionary()
#create list of french words 
Study_words = [i for i in Dict]

TIMER = window.after(0,func = flip_to_front)

window.mainloop()