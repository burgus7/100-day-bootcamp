print("Welcome to the BMI Calculator 2.0!")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight/(height ** 2))

verb = "are"

if bmi < 18.5:
    health = "underweight"
elif bmi < 25:
    health = "normal weight"
    verb = "have a"
elif bmi < 30:
    health = "slightly overweight"
elif bmi < 35:
    health = "obese"
else:
    health = "clinically obese"

print(f"Your BMI is {bmi}, you {verb} {health}")