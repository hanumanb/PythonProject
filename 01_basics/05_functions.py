"""Functions, defaults, keyword arguments, and return values."""
def calculate_monthly_cost(hourly_rate: float, hours: int = 730) -> float:
    if hourly_rate < 0 or hours < 0:
        raise ValueError("Rate and hours cannot be negative")
    return hourly_rate * hours

print(calculate_monthly_cost(0.12))
print(calculate_monthly_cost(hourly_rate=0.20, hours=100))
