# *arg -> Unlimited Arguments -> tuple

def add(*arg):
    sum = 0
    for a in arg:
        sum += a
    return sum

print(add(1, 2, 3))
print(add(1, 2, 3, 4))


# **kwargs -> Unlimited Positional / Keyword Arguments -> dict

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=3, multiply=5))



class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")






