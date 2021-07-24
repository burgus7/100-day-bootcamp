# Write your code below this line 👇

def prime_checker(number):
    is_prime = ""
    for i in range(2, number):
        if number % i == 0:
            is_prime = " not"

    print(f"It's{is_prime} a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



