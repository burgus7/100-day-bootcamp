print("Welcome to Life in Weeks")

age = input("What is your current age? ")
live_until = input("How old do you think you will live to be? ")

years = int(live_until) - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f"Assuming you live to be {live_until}, you have {days} days, {weeks} weeks, and {months} months left.")