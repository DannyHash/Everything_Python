"""
Your Task: Create a function called greet_target that:
Takes two parameters: target_ip and port
port should have a default value of 80
The function should print:
Initiating scan on 192.168.1.10:80...
"""


def greet_target(target_ip, port=80):
    print(f"Initiating scan on {target_ip}:{port}...")


greet_target("192.168.1.10")
greet_target("192.168.1.10", 443)
