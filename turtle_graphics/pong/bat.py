from turtle import Turtle


class Bat:

    def __init__(self, position):
        self.timmy = Turtle()
        self.timmy.shape("square")
        self.timmy.shapesize(4, 1)
        self.timmy.color("white")
        self.timmy.penup()
        self.timmy.speed("fastest")
        self.timmy.goto(position)

    def up(self):
        if self.timmy.ycor() < 240:
            self.timmy.goto(self.timmy.xcor(), self.timmy.ycor() + 20)

    def down(self):
        if self.timmy.ycor() > -240:
            self.timmy.goto(self.timmy.xcor(), self.timmy.ycor() - 20)
