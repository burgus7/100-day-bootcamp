import random
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user = int(input("What do you chose? Type:"
                 "\n0 for Rock"
                 "\n1 for Paper"
                 "\n2 for Scissors"
                 "\n-->"))
computer = randint(0,2)

offset = user - computer

if offset > 0:
    print (f"You Chose:\n{options[user]}Your opponent chose:\n {options[computer]}. You Lost!")
elif offset < 0:
    print(f"You Chose:\n{options[user]}Your opponent chose:\n {options[computer]}. You Won!")
else:
    print(f"You Chose:\n{options[user]}Your opponent chose:\n {options[computer]}. It's a Tie!")