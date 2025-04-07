"""
Tasks:
Create a list named xss_payloads with at least 5 common XSS payloads.
Add a new payload to the end of the list.
Insert a payload at the second position.
Remove one payload you think is redundant or weak.
Print the final list.
"""

xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert('XSS')>",
]

# Add a new payload to the end of the list
xss_payloads.append("<a href='javascript:alert(1)'>Click me</a>")
# Insert a payload at the second position
xss_payloads.insert(1, "<input type='text' onfocus=alert('XSS')>")
# Remove one payload you think is redundant or weak
xss_payloads.remove("<body onload=alert('XSS')>")
# Print the final list
print(xss_payloads)
