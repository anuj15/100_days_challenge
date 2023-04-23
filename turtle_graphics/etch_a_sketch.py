from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(20)


def backward():
    timmy.backward(20)


def left():
    timmy.left(20)


def right():
    timmy.right(20)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def etch_a_sketch():
    screen.listen()
    screen.onkey(fun=forward, key='a')
    screen.onkey(fun=backward, key='s')
    screen.onkey(fun=left, key='w')
    screen.onkey(fun=right, key='d')
    screen.onkey(fun=clear, key='c')
    exit_screen()


def exit_screen():
    screen.exitonclick()


if __name__ == "__main__":
    etch_a_sketch()
