import time
from turtle import Turtle


class Ball:

    def __init__(self):
        self.timmy = Turtle()
        self.timmy.penup()
        self.timmy.shape("circle")
        self.timmy.color("white")
        self.timmy.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.timer = 0.1

    def move(self):
        self.timmy.goto(self.timmy.xcor() + self.x_move, self.timmy.ycor() + self.y_move)
        time.sleep(self.timer)
        self.bounce()

    def bounce(self):
        if self.timmy.ycor() > 250 or self.timmy.ycor() < -250:
            self.y_move *= -1

    def left_miss(self):
        if self.timmy.xcor() <= -275:
            return True

    def right_miss(self):
        if self.timmy.xcor() >= 275:
            return True

    def hit(self):
        self.x_move *= -1

    def reset(self):
        self.timmy.goto(0, 0)
        self.timer = 0.1
        self.hit()

    def increase_speed(self):
        self.timer /= 2
