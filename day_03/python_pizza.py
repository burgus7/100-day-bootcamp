# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small = 15
medium = 20
large = 25

pepperoni_small = 2
pepperoni_med_large = 3
cheese = 1

total_bill = 0

if size == "S":
    total_bill = total_bill + small
    if add_pepperoni == "Y":
        total_bill = total_bill + pepperoni_small
elif size == "M":
    total_bill = total_bill + medium
    if add_pepperoni == "Y":
        total_bill =  total_bill + pepperoni_med_large
elif size == "L":
    total_bill = total_bill + large
    if add_pepperoni == "Y":
        total_bill =  total_bill + pepperoni_med_large

if extra_cheese == "Y":
    total_bill = total_bill + cheese

print (f"Your final bill is ${total_bill}")