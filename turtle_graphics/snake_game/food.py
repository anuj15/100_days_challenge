import random
from turtle import Turtle


class Food:
    food_turtle = Turtle()

    def create_food(self):
        self.food_turtle.goto(x=random.randint(-230, 230), y=random.randint(-230, 230))
        self.food_turtle.penup()
        self.food_turtle.color("blue")
        self.food_turtle.speed("fastest")
        self.food_turtle.shape("circle")
        self.food_turtle.turtlesize(.4)
