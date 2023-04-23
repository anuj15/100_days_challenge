from turtle import Turtle


def get_high_score():
    with open(file="high_score.txt") as f:
        return int(f.readline())


class Levels(Turtle):
    level = 0
    high_score = get_high_score()
    FONT = ("arial", 11, "bold")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 230)
        self.show_level()

    def show_level(self):
        self.write(f"Level: {self.level} High Score: {self.high_score}", move=False, align="left", font=self.FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        if self.level > self.high_score:
            self.high_score = self.level
            self.set_high_score()
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align="center", font=self.FONT)

    def set_high_score(self):
        with open(file="high_score.txt", mode="w") as f:
            f.write(str(self.high_score))
