"""Common collection types and when to use them."""
services = ["api", "payments", "api"]
immutable_region = ("us-east-1", "us-west-2")
unique_services = set(services)

services.append("inventory")
print("List:", services)
print("Tuple:", immutable_region)
print("Unique:", sorted(unique_services))
