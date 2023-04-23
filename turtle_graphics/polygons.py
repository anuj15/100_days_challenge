import random
import turtle
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()


def set_turtle():
    turtle.colormode(255)
    timmy.speed("fastest")
    timmy.shape("turtle")


def get_random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rbg = (r, b, g)
    return rbg


def draw_polygon():
    set_turtle()
    for i in range(3, 11):
        timmy.color(get_random_color())
        for j in range(1, i + 1):
            timmy.left(360 / i)
            timmy.forward(100)
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == '__main__':
    draw_polygon()
