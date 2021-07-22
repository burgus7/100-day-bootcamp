print("Welcome to the leap year calculator!")
year = int(input("Enter a year: "))
leap = "is not"

if year % 400 == 0:
    leap = "is"
elif year % 4 == 0 and year % 100 != 0:
    leap = "is"

print(f"{year} {leap} a leap year!")