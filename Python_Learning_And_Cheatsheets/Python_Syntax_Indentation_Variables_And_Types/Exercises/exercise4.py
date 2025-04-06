"""
Task:
Create a list of integers called numbers (e.g., [5, 12, 3, 21, 8, 17]).
Loop through the list and do the following for each number:
Print the number.
Check if it’s even or odd.
If it’s greater than 10, say "That's a big number!".
"""

numbers = [5, 12, 3, 21, 8, 17]

for number in numbers:
    print(f"Number: {number}")

    if number % 2 == 0:
        print("It's even")
    else:
        print("It's odd")

    if number > 10:
        print("That's a big number!")
    print()  # Print a newline for better readability

# The program creates a list of integers called numbers. It loops through the list, prints each number, checks if it's even or odd, and if it's greater than 10, it prints "That's a big number!".
