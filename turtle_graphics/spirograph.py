import random
import turtle
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()


def set_turtle():
    timmy.speed("fastest")
    turtle.colormode(255)
    timmy.shape("turtle")
    timmy.hideturtle()


def set_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


def draw_spirograph():
    set_turtle()
    for i in range(0, 361, 5):
        timmy.color(set_color())
        timmy.setheading(i)
        timmy.circle(100)
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == "__main__":
    draw_spirograph()
