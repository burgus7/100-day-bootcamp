import random

print("Welcome to the Coin Flipper!")
head_or_tail_num = random.randint(0,1)

if head_or_tail_num == 0:
    print ("Tails")
else:
    print("Heads")
