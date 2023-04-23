import random

from art import blackjack
from data import blackjack_cards

player = []
dealer = []
end_game = False
to_continue = True


def start_game():
    global end_game, to_continue
    while not end_game:
        for i in range(2):
            player.append(random.choice(blackjack_cards))
            dealer.append((random.choice(blackjack_cards)))
        print(f"Player cards: {player} Player score: {get_score(player)}")
        print(f"Dealer first card: {dealer[0]}")
        if get_score(player) == 21:
            print("BlackJack!")
            end_game = True
        else:
            while to_continue:
                choice = input("Draw or Fold? ").lower()
                if choice == 'draw':
                    add_card()
                else:
                    end_game = True
                    to_continue = False
                    find_winner()


def add_card():
    global end_game, to_continue
    player.append(random.choice(blackjack_cards))
    print(f"Player cards: {player} Player score: {get_score(player)}")
    if get_score(dealer) <= 17:
        dealer.append(random.choice(blackjack_cards))
    print(f"Dealer cards: {dealer} Dealer score: {get_score(dealer)}")
    if get_score(player) >= 21 or get_score(dealer) >= 21:
        end_game = True
        to_continue = False
        find_winner()


def get_score(user):
    score = 0
    for i in user:
        score += i
    if score > 21 and 11 in user:
        score -= 10
    return score


def find_winner():
    player_score = get_score(player)
    dealer_score = get_score(dealer)
    if 21 > player_score > dealer_score or (player_score == 21 and dealer_score != 21) or (
            player_score < 21 and dealer_score > 21):
        print(f"Player won!")
    elif 21 > dealer_score > player_score or player_score > 21 or (dealer_score == 21 and player_score != 21):
        print(f"Dealer won!")
    else:
        print("Draw!")


if __name__ == '__main__':
    print(blackjack)
    start_game()
