from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
scoring = Score()
food = Food()
snaky = Snake()


def set_screen():
    screen.setup(width=500, height=500)
    screen.bgcolor("black")
    screen.title("My Snake Game!")


def set_heading():
    screen.listen()
    screen.onkey(fun=snaky.up, key="Up")
    screen.onkey(fun=snaky.down, key="Down")
    screen.onkey(fun=snaky.right, key="Right")
    screen.onkey(fun=snaky.left, key="Left")


def eat_food():
    if snaky.snaky[0].distance(food.food_turtle) < 20:
        food.create_food()
        scoring.update_score()
        snaky.extend_tail()


set_screen()
scoring.show_score()
snaky.create_snake()
food.create_food()
set_heading()


def play_game():
    while not (snaky.self_hit() or snaky.wall_hit()):
        snaky.move_snake()
        eat_food()
    scoring.reset()
    snaky.reset()
    play_game()


if __name__ == '__main__':
    play_game()
    screen.exitonclick()
