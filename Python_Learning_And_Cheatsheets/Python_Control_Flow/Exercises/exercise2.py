"""
Problem:
Write a Python program that:
Asks the user to enter a number between 1 and 100.
Categorizes the number into:
"Low" if the number is between 1 and 30
"Medium" if between 31 and 70
"High" if between 71 and 100
If the number is outside this range, print "Out of range!"
"""

number = int(input("Please enter a number between 1 and 100:"))

if 1 <= number <= 30:
    print("Low")
elif 31 <= number <= 70:
    print("Medium")
elif 71 <= number <= 100:
    print("High")
else:
    print("Out of range!")
