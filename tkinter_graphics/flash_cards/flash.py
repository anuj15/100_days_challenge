import random
from tkinter import *

import pandas

FRENCH = "French"
ENGLISH = "English"
data = None
to_learn = {}
choice = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def show_french():
    global timer, choice
    choice = random.choice(to_learn)
    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=image_front)
    canvas.itemconfig(canvas_lang, text=FRENCH, fill="black")
    canvas.itemconfig(canvas_word, text=choice[FRENCH], fill="black")
    timer = window.after(5000, show_english)


def show_english():
    canvas.itemconfig(canvas_img, image=image_back)
    canvas.itemconfig(canvas_lang, text=ENGLISH, fill="white")
    canvas.itemconfig(canvas_word, text=choice[ENGLISH], fill="white")


def learnt_words():
    to_learn.remove(choice)
    pandas.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)
    show_french()


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, width=500, height=400, padx=10, pady=10)
timer = window.after(5000, show_french)

image_front = PhotoImage(file="card_front.png")
image_back = PhotoImage(file="card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=image_front)
canvas_lang = canvas.create_text(400, 130, text="Title", font=("ariel", 16, "italic"))
canvas_word = canvas.create_text(400, 200, text="Word", font=("ariel", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_yes = PhotoImage(file="right.png")
button_yes = Button(image=image_yes, command=learnt_words, bg=BACKGROUND_COLOR, border=0)
button_yes.grid(row=1, column=0)

image_no = PhotoImage(file="wrong.png")
button_no = Button(image=image_no, command=show_french, bg=BACKGROUND_COLOR, border=0)
button_no.grid(row=1, column=1)

window.mainloop()

if __name__ == '__main__':
    print("Start")
