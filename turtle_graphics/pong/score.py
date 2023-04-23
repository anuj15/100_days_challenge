from turtle import Turtle


class Score:
    score = 0

    def __init__(self, position):
        self.timmy = Turtle()
        self.timmy.hideturtle()
        self.timmy.color("white")
        self.timmy.speed("fastest")
        self.timmy.penup()
        self.initialize(position)

    def initialize(self, position):
        self.timmy.goto(position)
        self.timmy.write(f"{self.score}", move=False, align="left", font=("Arial", 36, "normal"))

    def update(self):
        self.timmy.clear()
        self.score += 1
        self.timmy.write(f"{self.score}", move=False, align="left", font=("Arial", 36, "normal"))
