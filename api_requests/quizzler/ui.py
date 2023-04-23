import html
import json
import random
from tkinter import *

import requests
import urllib3

score = 0
THEME_COLOR = "#375362"
base_url = "https://opentdb.com/api.php"
question_difficulty = ['easy', 'medium', 'hard']
question_type = ['boolean', 'multiple']
urllib3.disable_warnings()
categories = requests.get("https://opentdb.com/api_category.php", verify=False).json()["trivia_categories"]
with open(file="categories.json", mode='w') as f:
    json.dump(categories, f, indent=4)

parameters = {
    "amount": 3,
    "type": question_type[0],
    "difficulty": question_difficulty[0],
    "category": 11,
}
response = requests.get(base_url, params=parameters, verify=False)
response.raise_for_status()
questions_left = json.loads(json.dumps(response.json()["results"]))
with open(file="data.json", mode='w') as f:
    json.dump(questions_left, f, indent=4)
current_question = random.choice(questions_left)
questions_left.remove(current_question)
q = html.unescape(current_question["question"])
a = current_question["correct_answer"]


def click_right():
    select_answer("True")


def click_wrong():
    select_answer("False")


def select_answer(choice):
    global score, q, a
    if len(questions_left) > 0:
        if a == choice:
            score += 1
        question = random.choice(questions_left)
        questions_left.remove(question)
        q = html.unescape(question["question"])
        canvas.itemconfig(show_question, text=q)
        a = question["correct_answer"]
    else:
        canvas.itemconfig(show_question, text=f"Quiz over! Your final score is: {score}")
    label.config(text=f"Score: {score}")


window = Tk()
window.title("Quizzler")
window.config(padx=20, pady=20, bg=THEME_COLOR)

canvas = Canvas(width=300, height=350)
show_question = canvas.create_text(150, 150, text=q, font=("Arial", 16, "bold"), width=200)
canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)

label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 12, "bold"))
label.grid(row=0, column=1)

image_right = PhotoImage(file="images/true.png")
button_right = Button(image=image_right, border=0, highlightthickness=0, command=click_right)
button_right.grid(row=2, column=0)

image_wrong = PhotoImage(file="images/false.png")
button_wrong = Button(image=image_wrong, border=0, highlightthickness=0, command=click_wrong)
button_wrong.grid(row=2, column=1)

window.mainloop()

if __name__ == '__main__':
    print("")
