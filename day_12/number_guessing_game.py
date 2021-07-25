from number_guessing_game_art import logo
from frequent_functions import get_valid_answer
from random import randint

def number_guessing_game():
    print (logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = get_valid_answer(["easy", "hard"], "Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5

    target = randint(0, 100)

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        win = check_win(guess, target)
        print(win)
        if win =="Correct!":
            print("You win!")
            break
        if lives == 1:
            print(f"You lose. The number was {target}")
        print("Guess again.")
        lives -= 1

    again = get_valid_answer(["yes", "no"], "Do you want to play again? Type 'yes' or 'no': ")
    if again == "yes":
        number_guessing_game()
    elif again == "no":
        print("Okay, bye!")
        return


def check_win(guess, target):
    if guess > target:
        return "Too high."
    elif guess < target:
        return "Too low."
    else:
        return "Correct!"


number_guessing_game()