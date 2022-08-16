# 26.1
## Instructions
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

e.g. `4 * 4 = 16`
4 squared equals 16.
DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

## Example Output
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
##Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Make sure the squared_numbers is printed into the console for the code checking to work.

## Solution
https://repl.it/@appbrewery/day-26-1-solution

# 26.2
## Instructions
You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

##Example Output
[2, 8, 34]
##Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Even numbers can be divided by 2 with no remainder.

Remind yourself of how the modulo operator works.

## Solution
https://repl.it/@appbrewery/day-26-2-solution

# 26.3
💪 This exercise is HARD

## Instructions
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]
IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

## Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
## Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

First, you will need to read from the files and create a list using the lines in the files.

This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp

## Solution
https://repl.it/@appbrewery/day-26-3-solution

# 26.4
Dictionary Comprehension 1

## Instructions
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

## Example Output
{
'What': 4,
'is': 2,
'the': 3,
'Airspeed': 8,
'Velocity': 8,
'of': 2,
'an': 2,
'Unladen': 7,
'Swallow?': 8
}
## Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp

## Solution
https://repl.it/@appbrewery/day-26-4-solution

# 26.5
Dictionary Comprehension 2

##Instructions
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f:
(temp_c * 9/5) + 32 = temp_f
Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

##Example Output
{
'Monday': 53.6,
'Tuesday': 57.2,
'Wednesday': 59.0,
'Thursday': 57.2,
'Friday': 69.8,
'Saturday': 71.6,
'Sunday': 75.2
}
##Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get each of the items from a dictionary using the .items() method: https://www.w3schools.com/python/ref_dictionary_items.asp

##Solution
https://repl.it/@appbrewery/day-26-5-solution

