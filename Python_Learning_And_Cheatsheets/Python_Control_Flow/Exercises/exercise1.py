"""
Problem:
Write a Python program that:

Asks the user to input a number.

Checks if the number is even or odd.

Prints "Even Number" or "Odd Number" accordingly.
"""

number = int(input("Please enter a number:"))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
