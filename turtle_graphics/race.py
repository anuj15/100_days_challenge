import random
from turtle import Turtle, Screen

screen = Screen()

turtles = []
width = 500
height = 500


def set_screen():
    screen.setup(width=width, height=height)


def create_turtles():
    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    for i in range(1, 8):
        timmy = Turtle()
        timmy.shape("turtle")
        timmy.penup()
        timmy.color(colors[i - 1])
        timmy.setx(x=-width / 2 + 10)
        timmy.sety(y=-height / 2 + (50 * i))
        turtles.append(timmy)


def find_winner():
    while True:
        for i in range(len(turtles)):
            turtles[i].forward(random.randint(0, 10))
            if turtles[i].xcor() >= width / 2:
                return turtles[i].pencolor()


def start_race():
    set_screen()
    user_pick = screen.textinput(title="Place your bid!", prompt="Which color Turtle will win? ")
    create_turtles()
    winner = find_winner()
    if user_pick.lower() == winner.lower():
        print(f"You won! {winner.title()} turtle won the race.")
    else:
        print(f"You lose! {winner.title()} turtle won the race.")
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == "__main__":
    start_race()
