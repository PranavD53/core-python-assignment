class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


patients = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]

search_disease = "Flu"
result = []

for p in patients:
    if p.disease == search_disease:
        result.append(p.name)

print(f"Patients with {search_disease}:", result)
