"""
Problem:
Write a Python program that:
Repeatedly asks the user to enter a secret code using a while loop.
If the input is correct, print "Access Granted" and exit the loop.
If the input is wrong, print "Wrong code, try again."
"""

secret_code = "Hackers123"

while True:
    user_input = input("Please enter the secret code: ")

    if user_input == secret_code:
        print("Access Granted")
        break
    else:
        print("Wrong code, try again.")
        continue
