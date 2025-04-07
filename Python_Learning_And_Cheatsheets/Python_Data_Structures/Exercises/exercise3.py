"""
Create a dictionary called vuln_report where:
Keys are endpoint URLs.
Values are lists of vulnerabilities found on those endpoints.
Add a new vulnerability to an existing endpoint.
Add a new endpoint with its vulnerabilities.
Safely retrieve the list of vulnerabilities for a given endpoint.
Loop through the dictionary and print the full report.
"""

# Create a dictionary called vuln_report
vuln_report = {
    "/api/users": ["SQL Injection", "Cross-Site Scripting"],
    "/api/products": ["Cross-Site Scripting"],
    "/api/orders": ["Insecure Direct Object Reference"],
}
# Add a new vulnerability to an existing endpoint
vuln_report["/api/users"].append("Cross-Site Request Forgery")
# Add a new endpoint with its vulnerabilities
vuln_report["/api/payments"] = ["Sensitive Data Exposure"]
# Safely retrieve the list of vulnerabilities for a given endpoint


def get_vulnerabilities(endpoint):
    return vuln_report.get(endpoint, "No vulnerabilities found for this endpoint.")


# Example usage
print(get_vulnerabilities("/api/users"))

# Loop through the dictionary and print the full report
for endpoint, vulnerabilities in vuln_report.items():
    print(f"Endpoint: {endpoint}")
    print("Vulnerabilities:")
    for vuln in vulnerabilities:
        print(f"- {vuln}")
    print()
