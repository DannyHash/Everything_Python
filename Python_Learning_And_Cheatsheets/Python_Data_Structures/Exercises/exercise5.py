"""
Tasks:
Define a dictionary mapping endpoints to a list of vulnerabilities.
Create a set of all unique vulnerabilities across endpoints.
Create a list of tuples, where each tuple is (endpoint, vuln_count).
Print:
  Unique vulnerabilities
  Sorted list of endpoint-vuln summaries
"""

# Define a dictionary mapping endpoints to a list of vulnerabilities
vuln_report = {
    "/api/users": ["SQL Injection", "Cross-Site Scripting"],
    "/api/products": ["Cross-Site Scripting"],
    "/api/orders": ["Insecure Direct Object Reference"],
}
# Create a set of all unique vulnerabilities across endpoints
unique_vulnerabilities = set()

for vulnerabilities in vuln_report.values():
    unique_vulnerabilities.update(vulnerabilities)

# Create a list of tuples, where each tuple is (endpoint, vuln_count)
endpoint_vuln_count = [
    (endpoint, len(vulnerabilities))
    for endpoint, vulnerabilities in vuln_report.items()
]
# Print unique vulnerabilities
print("Unique Vulnerabilities:")
for vul in unique_vulnerabilities:
    print(f"- {vul}")

# Print sorted list of endpoint-vuln summaries
print("\nEndpoint Vulnerability Counts:")
for endpoint, count in sorted(endpoint_vuln_count, key=lambda x: x[1], reverse=True):
    print(f"{endpoint}: {count} vulnerabilities")

# Print the final report
print("\nFinal Report:")
for endpoint, vulnerabilities in vuln_report.items():
    print(f"Endpoint: {endpoint}")
    print("Vulnerabilities:")
    for vuln in vulnerabilities:
        print(f"- {vuln}")
    print()
