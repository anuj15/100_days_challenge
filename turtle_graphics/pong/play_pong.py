from turtle import Screen

from ball import Ball
from bat import Bat
from net import Net
from score import Score

screen = Screen()

screen.setup(width=600, height=550)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

net = Net()
l_bat = Bat((-280, 0))
r_bat = Bat((270, 0))
l_score = Score((-65, 225))
r_score = Score((20, 225))

ball = Ball()
game_is_on = True

screen.listen()
screen.onkey(fun=l_bat.up, key="a")
screen.onkey(fun=l_bat.down, key="z")
screen.onkey(fun=r_bat.up, key="Up")
screen.onkey(fun=r_bat.down, key="Down")

while game_is_on:
    screen.update()
    ball.move()
    if ball.right_miss():
        l_score.update()
        ball.reset()
    elif ball.left_miss():
        r_score.update()
        ball.reset()
    if ball.timmy.distance(r_bat.timmy) < 30 and ball.timmy.xcor() < 270:
        ball.hit()
        ball.increase_speed()
    elif ball.timmy.distance(l_bat.timmy) < 30 and ball.timmy.xcor() > -270:
        ball.hit()
        ball.increase_speed()

screen.exitonclick()

if __name__ == '__main__':
    print("Game Started")
