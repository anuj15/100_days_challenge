import random
import time
from turtle import Turtle


def colour():
    r = random.randint(50, 200)
    g = random.randint(50, 200)
    b = random.randint(50, 200)

    rgb = (r, g, b)
    return rgb


class Cars:
    X_START = 215
    Y_START = -180
    Y_END = 180
    EACH_STEP = 10
    SPEED = 0.2

    def __init__(self):
        self.car_list = []

    def move(self):
        for i in self.car_list:
            i.goto(i.xcor() - self.EACH_STEP, i.ycor())
        time.sleep(0.1)

    def increase_car_speed(self):
        self.SPEED *= 0.9

    def create_car(self, car_count):
        i = random.randint(1, car_count)
        if i % 5 == 0:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.turtlesize(1, 2.5)
            car.speed("fastest")
            car.color(colour())
            car.goto(self.X_START, random.randint(self.Y_START, self.Y_END))
            self.car_list.append(car)
