import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def set_turtle():
    turtle.colormode(255)
    timmy.shape("turtle")
    timmy.hideturtle()
    timmy.speed("fastest")
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(200)
    timmy.setheading(0)


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


def draw_hirst_painting():
    set_turtle()
    for i in range(10):
        for j in range(10):
            timmy.color(set_color())
            timmy.dot(15)
            timmy.forward(30)
        timmy.setheading(90)
        timmy.forward(30)
        timmy.setheading(180)
        timmy.forward(300)
        timmy.setheading(0)
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == "__main__":
    draw_hirst_painting()
