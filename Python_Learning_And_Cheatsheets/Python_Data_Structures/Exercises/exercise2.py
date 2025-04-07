"""
Create a list called scanned_domains with at least 10 domain strings, including some duplicates.
Convert it to a set to remove duplicates.
Convert the set back to a list and sort it alphabetically.
Print the cleaned, sorted list of unique domains.
"""

scanned_domains = [
    "example.com",
    "test.com",
    "example.org",
    "sample.net",
    "example.com",  # Duplicate
    "demo.com",
    "example.net",  # Duplicate
    "test.org",
    "sample.com",
    "demo.org",
]

# Convert the list to a set to remove duplicates
unique_domains = set(scanned_domains)
# Convert the set back to a list and sort it alphabetically
cleaned_domains = list(unique_domains)
# Sort the list alphabetically
cleaned_domains.sort()

print(cleaned_domains)
