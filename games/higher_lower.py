import random

from art import higher_lower, vs
from data import insta_followers


def print_logo():
    print(higher_lower)


def start_game():
    return input("Do you want to play higher or lower? Type 'y' or 'n' ").lower() == 'y'


def get_data():
    return random.choice(insta_followers)


def print_vs():
    print(vs)


def begin():
    print_logo()
    while start_game():
        end_game = False
        score = 0
        a = get_data()
        winner = a
        while not end_game:
            print(f"Name: {winner['name']}, a {winner['description']} from {winner['country']}")
            print_vs()
            b = get_data()
            while b == winner:
                b = get_data()
            print(f"Name: {b['name']}, a {b['description']} from {b['country']}")
            choice = input(f"Are followers of {winner['name']} Higher or Lower than the followers of {b['name']}? "
                           f"Type 'higher' or 'lower' ").lower()
            if winner['follower_count'] > b['follower_count'] and choice == 'higher':
                score += 1
                print(f"Right answer! Your current score is {score}")
            elif winner['follower_count'] < b['follower_count'] and choice == 'lower':
                winner = b
                score += 1
                print(f"Right answer! Your current score is {score}")
            else:
                print(f"Wrong answer! Your final score is {score}")
                end_game = True


if __name__ == '__main__':
    begin()
