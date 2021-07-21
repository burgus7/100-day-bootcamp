from random import sample

def format_text(string_in):
    string_out = string_in[0].upper()

    for i in range(1, len(string_in)):
        if string_in[i-1] == " ":
            string_out = string_out + string_in[i].upper()
        else:
            string_out = string_out + string_in[i].lower()
    return string_out

questions = ["What is the name of the city you grew up in?\n",
             "What is your favorite color?\n",
             "What is/was your pet's name?\n",
             "What is your favorite animal?\n",
             "What elementary school did you go to?\n"]

print("Welcome to Band Name Generator")

question_index = sample(range(0, len(questions)), 2)

answer1 = format_text(input(questions[question_index[0]]))
answer2 = format_text(input(questions[question_index[1]]))

print(f"Your band name could be {answer1} {answer2}")
