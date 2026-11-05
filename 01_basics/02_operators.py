"""Arithmetic, comparison, and logical operators."""
cpu_percent = 87
memory_percent = 92

print("Average utilization:", (cpu_percent + memory_percent) / 2)
print("CPU critical:", cpu_percent >= 90)
print("Memory warning:", memory_percent >= 85 and memory_percent < 95)
print("At least one warning:", cpu_percent >= 80 or memory_percent >= 80)
