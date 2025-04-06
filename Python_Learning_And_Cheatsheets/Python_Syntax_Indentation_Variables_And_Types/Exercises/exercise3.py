"""
Task:
Ask the user for their birth year using input().
Convert the birth year into an integer.
Calculate their age (assume current year is 2025).
Check if the person is:
A teenager (13–19),
An adult (20 and above),
Or too young (below 13).
Print their age and category using a clean output format.
"""

birth_year = input("Please enter your birth year:")
birth_year = int(birth_year)
current_year = 2025
age = current_year - birth_year

if age < 13:
    category = "too young"
elif 13 <= age <= 19:
    category = "a teenager"
else:
    category = "an adult"

print(f"You are {age} years old and you are {category}")

# The program asks the user for their birth year, converts it into an integer, calculates their age, checks their category, and prints the result in a clean format.
