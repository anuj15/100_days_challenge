from turtle import Turtle

FONT = ("Arial", 12, "normal")
ALIGN = "center"
COLOR = "white"
SPEED = "fastest"
FILE = "high_score.txt"


def get_high_score():
    with open(file=FILE, mode='r') as f:
        return int(f.readline())


class Score:
    score = 0
    highest_score = get_high_score()
    snake_score = Turtle()

    def show_score(self):
        self.snake_score.goto(0, 220)
        self.snake_score.speed(SPEED)
        self.snake_score.penup()
        self.snake_score.hideturtle()
        self.snake_score.color(COLOR)
        self.snake_score.write(f"Score = {self.score} High Score = {self.highest_score}", move=False, align=ALIGN,
                               font=FONT)

    def update_score(self):
        self.score += 1
        self.snake_score.clear()
        self.snake_score.write(f"Score = {self.score} High Score = {self.highest_score}", move=False, align=ALIGN,
                               font=FONT)

    def game_over(self):
        self.snake_score.goto(0, 0)
        self.snake_score.write(f"Game Over. Final Score = {self.score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.set_high_score()
        self.score = 0
        self.snake_score.clear()
        self.snake_score.write(f"Score = {self.score} High Score = {self.highest_score}", move=False, align=ALIGN,
                               font=FONT)

    def set_high_score(self):
        with open(file=FILE, mode='w') as f:
            f.write(str(self.highest_score))
