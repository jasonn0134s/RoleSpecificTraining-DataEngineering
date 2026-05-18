import json

data = {
    "students": [
        {"name": "Priya", "marks": 88},
        {"name": "Karan", "marks": 75}
    ]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)