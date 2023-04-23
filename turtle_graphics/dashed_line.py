from turtle import Screen, Turtle

screen = Screen()
timmy = Turtle()


def set_turtle():
    timmy.shape("turtle")
    timmy.speed("fastest")
    timmy.color("red")


def draw_dash_line():
    set_turtle()
    for _ in range(20):
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()
        timmy.forward(5)
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == '__main__':
    draw_dash_line()
