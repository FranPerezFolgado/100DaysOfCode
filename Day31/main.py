from cProfile import label
from cgitb import text
from email.mime import image
from time import sleep
from tkinter import *
from tkinter.font import BOLD, ITALIC 
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FLASHCARD_IMAGE_FRONT = 'Day31/images/card_front.png'
FLASHCARD_IMAGE_BACK = 'Day31/images/card_back.png'
RIGHT_IMAGE = 'Day31/images/right.png'
WRONG_IMAGE = 'Day31/images/wrong.png'
DATA_FILE = 'Day31/data/english_words.csv'

def change_word():
    selected_word = choice(word_dict)
    word_english = selected_word['English']
    if  word_english in used_words:
        change_word()
    else:
        used_words.append(word_english)
        flashcard.itemconfigure(lbl_word, text=word_english)

words = pandas.read_csv(DATA_FILE)
word_dict = words.to_dict(orient="records")
used_words = []


root = Tk()
root.title('Flashy')
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flashcard = Canvas(width=810,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file=FLASHCARD_IMAGE_FRONT)
flashcard.create_image(400,265, image=flashcard_front)

lbl_language = flashcard.create_text(400,150, text='English',font=("Courier",40, ITALIC))
lbl_word= flashcard.create_text(400,263, font=("Courier",60, BOLD))
change_word()

flashcard.grid(row=0,column=0,columnspan=2)

img_right = PhotoImage(file=RIGHT_IMAGE)
btn_right = Button(image=img_right, highlightthickness=0,borderwidth=0,command=change_word)
btn_right.grid(row=1,column=0)

img_wrong = PhotoImage(file=WRONG_IMAGE)
btn_wrong= Button(image=img_wrong, highlightthickness=0,borderwidth=0,command=change_word)
btn_wrong.grid(row=1,column=1)


root.mainloop()