"""
Problem:
Write a Python program that:
Asks the user for a positive number N.
Uses a for loop to calculate the sum of all numbers from 1 to N.
Prints the result.
"""

n = int(input("Please enter a positive number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(f"The sum of all numbers from 1 to {n} is {sum}")
