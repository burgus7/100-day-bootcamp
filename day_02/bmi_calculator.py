print("Welcome to the BMI Calculator!")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight/(height ** 2))
print(f"Your BMI is {bmi}!")