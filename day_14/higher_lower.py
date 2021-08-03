from higher_lower_art import logo, vs
from random import sample
from higher_lower_game_data import data
from frequent_functions import get_valid_answer

score = 0
while True:
    print(logo)

    players = sample(data, 2)

    print(f"Compare A: {players[0]['name']}, a {players[0]['description']}, from {players[0]['country']}")
    print(vs)
    print(f"Compare B: {players[1]['name']}, a {players[1]['description']}, from {players[1]['country']}")
    guess = get_valid_answer(["A", "B"], "Who has more followers? Type 'A' or 'B': ")

    if players[0]['follower_count'] > players[1]['follower_count']:
        answer = 'A'
    else:
        answer = 'B'

    if guess == answer:
        score += 1
        print(f"Correct, your score is {score}!")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break


