import time
from turtle import Turtle


class Snake:
    snaky = []

    def add_snake(self):
        timmy = Turtle()
        timmy.penup()
        timmy.color("white")
        timmy.shape("square")
        timmy.speed("fastest")
        timmy.turtlesize(0.7)
        return timmy

    def create_snake(self):
        snake_x_pos = 0
        for i in range(3):
            timmy = self.add_snake()
            timmy.goto(x=snake_x_pos, y=0)
            snake_x_pos -= 20
            self.snaky.append(timmy)

    def extend_tail(self):
        timmy = self.add_snake()
        timmy.goto(self.snaky[len(self.snaky) - 1].position())
        self.snaky.append(timmy)

    def move_snake(self):
        for i in range(len(self.snaky) - 1, 0, -1):
            self.snaky[i].goto(self.snaky[i - 1].position())
        self.snaky[0].forward(20)
        time.sleep(0.1)

    def up(self):
        if self.snaky[0].heading() != 270:
            self.snaky[0].setheading(90)

    def down(self):
        if self.snaky[0].heading() != 90:
            self.snaky[0].setheading(270)

    def right(self):
        if self.snaky[0].heading() != 180:
            self.snaky[0].setheading(0)

    def left(self):
        if self.snaky[0].heading() != 0:
            self.snaky[0].setheading(180)

    def self_hit(self):
        for i in range(1, len(self.snaky)):
            if self.snaky[0].position() == self.snaky[i].position():
                return True

    def wall_hit(self):
        if self.snaky[0].xcor() < -225 or self.snaky[0].xcor() > 225 or self.snaky[0].ycor() < -225 or \
                self.snaky[0].ycor() > 225:
            return True

    def reset(self):
        for i in self.snaky:
            i.goto(1000000, 1000000)
        self.snaky = []
        self.create_snake()
