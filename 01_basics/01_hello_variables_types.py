"""Variables, basic types, input, and formatted output."""
name = "Deloitte Candidate"
years_experience = 15
cloud_engineer = True
skills = ["Python", "Java", "AWS", "Kubernetes"]

print(f"Name: {name}")
print(f"Experience: {years_experience} years")
print(f"Cloud engineer: {cloud_engineer}")
print("Skills:", ", ".join(skills))
print("Types:", type(name).__name__, type(years_experience).__name__)
