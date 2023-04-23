from turtle import Turtle


class Net:

    def __init__(self):
        self.timmy = Turtle()
        self.timmy.color("white")
        self.timmy.hideturtle()
        self.timmy.speed("fastest")
        self.timmy.pensize(5)
        self.draw(270)
        self.draw(90)

    def draw(self, heading):
        self.timmy.setheading(heading)
        for i in range(8):
            self.timmy.pendown()
            self.timmy.forward(20)
            self.timmy.penup()
            self.timmy.forward(20)
        self.timmy.goto(0, 0)
