#!/usr/bin/python3
"""This program will assign a random signed number to the variable number each
time it is executed.
Print the last digit of the number stored in the variable number"""

import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
# YOUR CODE HERE
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    appended_string = "and is greater than 5"
if last_digit == 0 or number == 0:
    appended_string = "and is 0"
if last_digit < 6 and not 0:
    appended_string = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {appended_string}")
