"""for/while loops and enumerate."""
services = ["api", "payments", "inventory"]
for index, service in enumerate(services, start=1):
    print(f"{index}. checking {service}")

retry_count = 0
max_retries = 3
while retry_count < max_retries:
    retry_count += 1
    print(f"Attempt {retry_count}")
