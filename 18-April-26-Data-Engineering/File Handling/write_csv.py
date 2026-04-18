import csv

data = [
    ["name", "marks"],
    ["Priya", 88],
    ["Karan", 75]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)