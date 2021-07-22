from random import choices

print("Welcome to the Banker Roulette!")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{choices(names)[0]} will pay for everyone's meal!")