print("Welcome to the Digit Summing Program! ")

in_num = input("Enter a two digit number: ")
sum = 0

for num in in_num:
    sum = sum + int(num)

print(sum)