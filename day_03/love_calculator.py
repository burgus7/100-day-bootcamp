print("Welcome to the Love Calculator")

user_name = input("What is your name? \n").lower()
partner_name = input("What is your partner's name? \n").lower()

tens = 0
for i in "true":
    tens = tens + user_name.count(i)
    tens = tens + partner_name.count(i)

ones = 0
for i in "love":
    ones = ones + user_name.count(i)
    ones = ones + partner_name.count(i)

score = tens*10 + ones

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together!")
else:
    print(f"Your score is {score}!")