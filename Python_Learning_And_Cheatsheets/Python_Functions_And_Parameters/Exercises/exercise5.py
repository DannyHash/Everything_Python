"""
Your Task:
Create a function called build_request that:
Accepts three parameters: url, method, and an optional headers dictionary (defaults to empty {})
It should return a string that formats the request like:

```pgsql
Sending a GET request to https://target.com with headers: {'User-Agent': 'H4ck3r'}
```

If headers aren’t provided, use an empty dictionary
"""


def build_request(url, method, headers=None):
    if headers is None:
        headers = {}
    return f"Sending a {method.upper()} request to {url} with headers: {headers}"


custom_headers = {"User-Agent": "H4ck3r", "Authorization": "Bearer deadbeef"}

print(build_request("https://target.com", "GET", custom_headers))
print(build_request("https://target.com/api", "post"))
