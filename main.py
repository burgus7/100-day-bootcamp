import os
from frequent_functions import get_valid_answer
def main():
    valid_answers = []
    for i in range(1, 101):
        if i < 10:
            valid_answers.append(f"0{i}")
        else:
            valid_answers.append(str(i))

    day_num = get_valid_answer(valid_answers, "What day do you want to see? Enter a number 01-100: ")
    folder = f"day_{day_num}"
    filename = input("Which program would you like to run?")
    os.system(f"python {folder}\{filename}")

main()