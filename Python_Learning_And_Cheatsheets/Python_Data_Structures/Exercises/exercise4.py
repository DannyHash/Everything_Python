"""
Write a function analyze_url(url) that:
Extracts query parameters using urllib.parse.
Returns a tuple: (param_count, param_names, domain)
Call the function with a test URL.
Unpack the returned tuple and print the results nicely.
"""

from urllib.parse import urlparse, parse_qs


def analyze_url(url):
    # Parse the URL
    parsed_url = urlparse(url)
    # Extract query parameters
    query_params = parse_qs(parsed_url.query)
    # Count the number of parameters
    param_count = len(query_params)
    # Get parameter names
    param_names = list(query_params.keys())
    # Get the domain
    domain = parsed_url.netloc
    # Return a tuple with the results
    return param_count, param_names, domain


# Example URL
test_url = "https://example.com/search?q=python&lang=en&sort=asc"
# Call the function
param_count, param_names, domain = analyze_url(test_url)
# Print the results
print(f"Parameter Count: {param_count}")
print(f"Parameter Names: {param_names}")
print(f"Domain: {domain}")
