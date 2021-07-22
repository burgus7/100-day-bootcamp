print("Welcome to the Tip Calculator!")
bill = input("What was the total bill? $")
num_people = input("How many people will split the bill? ")
percentage = input("What percentage tip would you like to give? ")

per_person = (float(bill) * (1 + float(percentage)/100)) / int(num_people)
per_person = "{:.2f}".format(per_person)
print(f"Each person will pay ${per_person}")