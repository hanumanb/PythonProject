"""Sort structured data using a key function."""
incidents = [
    {"service": "catalog", "severity": "LOW", "count": 4},
    {"service": "payments", "severity": "CRITICAL", "count": 1},
    {"service": "orders", "severity": "HIGH", "count": 7},
]
rank = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
for item in sorted(incidents, key=lambda x: (rank[x["severity"]], -x["count"])):
    print(item)
