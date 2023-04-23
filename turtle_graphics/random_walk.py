import random
import turtle
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
directions = [0, 90, 180, 270]


def set_turtle():
    timmy.speed("fastest")
    timmy.shape("turtle")
    turtle.colormode(255)
    turtle.hideturtle()
    timmy.pensize(10)


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_random_walk():
    set_turtle()
    for i in range(200):
        timmy.color(set_color())
        timmy.forward(15)
        timmy.setheading(random.choice(directions))
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == "__main__":
    draw_random_walk()
