"""Dictionaries: common interview pattern."""
server = {"name": "app-01", "status": "healthy", "cpu": 78}
server["memory"] = 84

for key, value in server.items():
    print(f"{key}: {value}")

print("Missing key default:", server.get("owner", "unassigned"))
