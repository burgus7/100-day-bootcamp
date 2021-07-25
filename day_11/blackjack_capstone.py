from blackjack_art import logo
from random import choice
def get_valid_answer(valid_answers, prompt):
    while True:
        play = input(prompt)
        if play in valid_answers:
            return play
        else:
            print("Invalid answer, try again!")


cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]

def deal_cards():
    """returns a random card"""
    return(choice(cards))


def calculate_score(cards):
    """takes list of cards in hand and calculates score"""
    score = 0
    for card in cards:
        if card == "Ace":
            value_drawn = 11 # will check later if 1 is better
        elif type(card) == str:
            value_drawn = 10
        else:
            value_drawn = card
        score += value_drawn

    if "Ace" in cards and score > 21:
        score -= 10

    return score


def get_winner(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    result = ""
    if user_score > 21 and computer_score > 21:
        result = "Both players bust. No winner!"
    elif user_score > 21:
        result = "Computer won, user bust!"
    elif computer_score > 21:
        result = "User won, computer bust!"
    elif computer_score > user_score:
        result = "Computer won!"
    elif user_score > computer_score:
        result = "User won!"
    else:
        result = "Draw!"
    return result


def play_game():
    play = get_valid_answer(['y', 'n'], "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        print("Okay, bye!")
        return

    print(logo)
    user_cards = [deal_cards()]
    user_cards.append(deal_cards())
    print(f"Your cards: {user_cards}")
    print(f"Your current score is: {calculate_score(user_cards)}")
    computer_cards = [deal_cards()]
    print(f"Computer's first card: {computer_cards}")

    while True:
        if calculate_score(computer_cards) < 17:
            computer_cards.append(deal_cards())

        another = get_valid_answer(['y', 'n'], "Type 'y' to get another card, type 'n' to pass: ")
        if another == 'n':
            print(f"Your final hand is: {user_cards}")
            print(f"Computer's final hand is: {computer_cards}")

            print(get_winner(user_cards, computer_cards))
            break

        user_cards.append(deal_cards())
        print(f"Your cards: {user_cards}")
        print(f"Computer's cards: {computer_cards}")
    play_game()


play_game()

