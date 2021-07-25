############DEBUGGING#####################

# Describe Problem
def describe_the_problem():
    def my_function():
        for i in range(1, 21):
            if i == 20:
                print("You got it")
    my_function()

# Reproduce the Bug
def reproduce_the_bug():
    from random import randint
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 5)
    print(dice_imgs[dice_num])

# Play Computer
def play_computer():
    year = int(input("What's your year of birth?"))
    if year > 1980 and year < 1994:
        print("You are a millenial.")
    elif year > 1994:
        print("You are a Gen Z.")

# Fix the Errors
def fix_the_errors():
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")

#Print is Your Friend
def printing_is_your_friend():
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(total_words)

#Use a Debugger
def use_a_debugger():
    def mutate(a_list):
        b_list = []
        for item in a_list:
            new_item = item * 2
            b_list.append(new_item)
        print(b_list)

    mutate([1, 2, 3, 5, 8, 13])

##############PROGRAMS################

def even_odd():
    number = int(input("Which number do you want to check?"))

    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def leap_year():
    year = int(input("Which year do you want to check?"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

