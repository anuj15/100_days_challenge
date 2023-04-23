from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
timmy.hideturtle()
timmy.fillcolor("green")
timmy.begin_fill()


def star():
    x = 60
    timmy.setheading(x)
    timmy.forward(x)
    timmy.setheading(0)
    timmy.forward(x)
    timmy.setheading(2 * x)
    timmy.forward(x)
    timmy.setheading(x)
    timmy.forward(x)
    timmy.setheading(3 * x)
    timmy.forward(x)
    timmy.setheading(2 * x)
    timmy.forward(x)
    timmy.setheading(4 * x)
    timmy.forward(x)
    timmy.setheading(3 * x)
    timmy.forward(x)
    timmy.setheading(5 * x)
    timmy.forward(x)
    timmy.setheading(4 * x)
    timmy.forward(x)
    timmy.setheading(0)
    timmy.forward(x)
    timmy.setheading(5 * x)
    timmy.forward(x)


def pacman():
    timmy.setheading(270)
    timmy.forward(60)
    timmy.setheading(0)
    timmy.circle(60, 270)


timmy.end_fill()
screen.exitonclick()

if __name__ == '__main__':
    print("begin")
