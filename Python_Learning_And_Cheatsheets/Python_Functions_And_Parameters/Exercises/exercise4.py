"""
Your Task: Write a function called fuzz_inputs that:
Accepts any number of payloads using *args
Loops through each one and prints:
Injecting payload: <payload>
"""


def fuzz_inputs(*args):
    for payload in args:
        print(f"Injecting payload: {payload}")


fuzz_inputs("payload1", "payload2", "payload3")
