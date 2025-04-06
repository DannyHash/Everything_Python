"""
Write a Python script that:
Takes user's name and birth year via input.
Calculates their age (assume it’s 2025).
Stores a list of random numbers.
Loops through the numbers to:
Print whether each is even/odd.
Count how many numbers are greater than the person’s age.
Use functions to:
Greet the user.
Calculate age.
Analyze the number list.
"""


def greet_user(name):
    print(f"Hello, {name}! Welcome to the program")
    return


def calculate_age(birth_year):
    current_year = 2025
    age = current_year - birth_year
    return age


def analyze_numbers(numbers, age):
    even_count = 0
    odd_count = 0
    greater_than_age_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
            print(f"{number} is even")
        else:
            odd_count += 1
            print(f"{number} is odd")

        if number > age:
            greater_than_age_count += 1
            print(f"{number} is greater than your age")

        print()
        print(f"Total even numbers: {even_count}")
        print(f"Total odd numbers: {odd_count}")
        print(f"Total numbers greater than your age: {greater_than_age_count}")
        print()


# Main program

name = input("Enter your name:")
birth_year = int(input("Enter your birth year:"))
print()

greet_user(name)

age = calculate_age(birth_year)
print(f"You are {age} years old")
print()

numbers = [10, 21, 30, 41, 15]

analyze_numbers(numbers, age)

# The program takes user's name and birth year via input, calculates their age, stores a list of random numbers, loops through the numbers, and analyzes them.
