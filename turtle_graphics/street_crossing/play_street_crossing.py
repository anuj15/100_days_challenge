from turtle import Screen

from cars import Cars
from levels import Levels
from timmy import Crosser

screen = Screen()


def setup_screen():
    screen.title("Street Crossing Game!")
    screen.setup(width=500, height=500)
    screen.colormode(255)
    screen.tracer(0)


setup_screen()
timmy = Crosser()
level = Levels()
car = Cars()
game_is_on = True
car_count = 25


def listen_key_press():
    screen.listen()
    screen.onkey(fun=timmy.start_crossing, key="Up")


while game_is_on:
    screen.update()
    listen_key_press()
    car.create_car(car_count)
    car.move()
    for i in car.car_list:
        if timmy.distance(i) < 25:
            game_is_on = False
            level.game_over()
    if timmy.complete_crossing():
        level.increase_level()
        car.increase_car_speed()
        timmy.start_new_level()
        car_count -= 1

screen.exitonclick()

if __name__ == '__main__':
    print("Game Started")
