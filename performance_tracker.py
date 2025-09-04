class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.avg = 0

    def calc_avg(self):
        total = 0
        for m in self.marks:
            total += m
        self.avg = round(total / len(self.marks), 2)
        return self.avg

data = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

avg = {}
top = None
top_avg = 0

for name in data:
    s = Student(name, data[name])
    a = s.calc_avg()
    avg[name] = a
    if a > top_avg:
        top_avg = a
        top = s

print("Average Marks:", avg)
print(f"Top Performer: {top.name}")
