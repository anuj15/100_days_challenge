from turtle import Turtle


class Crosser(Turtle):
    START_X = 0
    START_Y = -230
    END_Y = 230
    EACH_STEP = 10
    NORTH = 90

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(self.START_X, self.START_Y)
        self.shape("turtle")
        self.speed("fastest")
        self.setheading(self.NORTH)

    def start_crossing(self):
        if self.ycor() < self.END_Y:
            self.goto(self.xcor(), self.ycor() + self.EACH_STEP)

    def complete_crossing(self):
        if self.ycor() == self.END_Y:
            self.start_new_level()
            return True

    def start_new_level(self):
        self.goto(self.START_X, self.START_Y)
