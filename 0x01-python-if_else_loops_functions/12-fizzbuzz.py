#!/usr/bin/python3
"""
This module contains the fizzbuzz function that prints numbers from 1 to 100
separated by a space, replacing multiples of 3 with 'Fizz', multiples of 5 with
'Buzz', and multiples of both with 'FizzBuzz'.
"""


def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space, replacing multiples
    of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with
    'FizzBuzz'.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == "__main__":
    fizzbuzz()
