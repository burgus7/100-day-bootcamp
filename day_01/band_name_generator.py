
def format_text(string_in):
    string_out = string_in[0].upper()

    for i in range(1, len(string_in)):
        if string_in[i-1] == " ":
            string_out = string_out + string_in[i].upper()
        else:
            string_out = string_out + string_in[i].lower()
    return string_out

print("Welcome to Band Name Generator")
city = format_text(input("What is the name of the city you grew up in?\n"))
pet = format_text(input("What is/was your pet's name?\n"))
print(f"Your band name could be {city} {pet}")
