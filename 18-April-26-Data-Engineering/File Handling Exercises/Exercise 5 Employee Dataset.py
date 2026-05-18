import csv

with open("employees.csv", "r") as f:
    data = list(csv.DictReader(f))

for e in data:
    print(e["name"])

for e in data:
    if e["department"] == "IT":
        print(e["name"])

avg = sum(int(e["salary"]) for e in data) / len(data)
print("Average salary:", avg)

top = max(data, key=lambda x: int(x["salary"]))
print("Highest salary:", top["name"])

dept = {}
for e in data:
    d = e["department"]
    dept[d] = dept.get(d, 0) + 1

print(dept)