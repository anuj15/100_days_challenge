import random

from art import guess_number

EASY_CHOICES = 10
HARD_CHOICES = 5
continue_play = True


def get_number():
    return random.randint(1, 100)


def print_logo():
    print(guess_number)


def play_game(number, level):
    lives = level
    print(f"You have {level} attempts to guess the correct number. All the best!")
    for i in range(level):
        guess = int(input(f'Guess the number: '))
        lives -= 1
        if guess == number:
            print(f"You won! The correct answer is {number}")
            return
        elif guess > number:
            print(f"Too high. Attempts remaining: {lives}")
        else:
            print(f"Too low. Attempts remaining: {lives}")
    print(f"Game Over! The correct answer was {number}")
    start_game()


def start_game():
    global continue_play
    num = get_number()
    while continue_play:
        level = input("Do you want to play the guessing game? Type 'e' for easy level, 'h' for hard level and any "
                      "other key to quit: ").lower()
        if level == 'e':
            play_game(num, EASY_CHOICES)
        elif level == 'h':
            play_game(num, HARD_CHOICES)
        else:
            continue_play = False


if __name__ == '__main__':
    print_logo()
    start_game()
