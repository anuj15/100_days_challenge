import random

from art import hangman_logo, hangman_stages
from data import movie_names, alphabets


def show_logo():
    print(hangman_logo)


class Hangman:

    def __init__(self):
        self.continue_play = True
        self.lives = 6
        self.blank_list = []

    def start_game(self):
        show_logo()
        start_game = input("Do you want to play HANGMAN? Type 'Yes' or 'No': ")
        if start_game.lower() != 'yes':
            self.continue_play = False
        else:
            movie_name = random.choice(movie_names).lower()
            print(f"Pssst! The correct answer is {movie_name}")
            for i in movie_name:
                if i in alphabets:
                    self.blank_list.append("_ ")
                elif i == " ":
                    self.blank_list.append("     ")
                else:
                    self.blank_list.append(i)
            print("".join(self.blank_list))
            print(hangman_stages[self.lives])
            self.continue_game(movie_name)
            self.start_game()

    def continue_game(self, movie_name):
        while self.continue_play:
            guessed_char = input("Guess a letter: ")
            if guessed_char in movie_name:
                if guessed_char in self.blank_list:
                    print(f"You've already guessed {guessed_char}. Lives remaining: {self.lives}")
                else:
                    print(f"{guessed_char} is in movie name. Lives remaining: {self.lives}")
                    for i in range(len(movie_name)):
                        if movie_name[i] == guessed_char:
                            self.blank_list[i] = movie_name[i]
                    if "".join(self.blank_list).replace(" ", "") == movie_name.replace(" ", ""):
                        self.continue_play = False
                        print(f"You Won! The correct name was {movie_name}")
            else:
                self.lives -= 1
                print(f"{guessed_char} is not in movie name. Lives remaining: {self.lives}")
                if self.lives == 0:
                    self.continue_play = False
                    print(f"You Lose! The correct name was {movie_name}")
            print("".join(self.blank_list))
            print(hangman_stages[self.lives])


if __name__ == '__main__':
    hangman = Hangman()
    hangman.start_game()
