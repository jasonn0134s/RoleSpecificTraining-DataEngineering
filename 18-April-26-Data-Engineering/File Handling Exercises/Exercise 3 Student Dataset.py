import json

with open("students.json", "r") as f:
    data = json.load(f)

students = data["students"]

for s in students:
    print(s["name"])

for s in students:
    if s["course"] == "Python":
        print(s["name"])

top = max(students, key=lambda x: x["marks"])
print("Topper:", top["name"])

avg = sum(s["marks"] for s in students) / len(students)
print("Average:", avg)

course_count = {}
for s in students:
    c = s["course"]
    course_count[c] = course_count.get(c, 0) + 1

print(course_count)