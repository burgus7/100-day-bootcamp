'''List Comprehension Tutorial'''
# old_list = [x, y, z]
# new_list = [new_number for item in old_list]

''' Add one '''
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Shweta"
new_list = [letter for letter in name]
print(new_list)

''' Double numbers in range '''
doubled = [n * 2 for n in range(1, 5)]
print(doubled)

''' List comprehension with if key word '''
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
name_len = 5
short_names = [name for name in names if len(name) < name_len]
long_names_caps = [name.upper() for name in names if len(name) >= name_len]

print(short_names)
print(long_names_caps)

''' Squaring Numbers - 26.1 '''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(numbers)
print(squared_numbers)

''' Filter Even Numbers - 26.2 '''
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

''' Get common numbers - 26.3 '''
import pandas as pd
file1_data = pd.read_csv('file1.txt')
file2_data = pd.read_csv('file2.txt')
common_numbers = [int(n) for n in file1_data if n in file2_data]
print(common_numbers)

''' Dictionary Comprehension - 26.4 '''
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

''' Dictionary Comprehension 2 - 26.5 '''
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def c_to_f(temp_c):
    temp_f = (temp_c * 9 / 5) + 32
    return temp_f

# weather_f = {day:c_to_f(weather_c[day]) for day in weather_c}
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)





