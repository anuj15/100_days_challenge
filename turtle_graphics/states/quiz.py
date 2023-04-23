import turtle
from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.title("Indian States")
screen.addshape("India.gif")
turtle.shape("India.gif")
timmy = Turtle()
timmy.hideturtle()
timmy.penup()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


score = 0
STATES = 28
correct_answers = []
s = pandas.read_csv("states.csv")
states = s.States
state_list = states.to_list()

while score < 29:
    answer = screen.textinput(title=f"Guess the state {score}/{STATES}", prompt="What's another state name?").title()
    if answer in state_list and answer not in correct_answers:
        score += 1
        correct_answers.append(answer)
        x_cor = s[states == answer].x
        y_cor = s[states == answer].y
        timmy.goto(int(x_cor.iloc[0]), int(y_cor.iloc[0]))
        timmy.write(answer, font=("arial", 8, "bold"))
    elif answer == "Exit":
        break

states_to_learn = [x for x in state_list if x not in correct_answers]
to_learn = pandas.DataFrame(states_to_learn)
to_learn.to_csv("states_to_learn.csv")

print(f"Your score is {score}")

if __name__ == '__main__':
    print("Start Quiz")
