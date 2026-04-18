student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])

print(student.get("name"))
print(student.get("course"))

student["city"] = "Hyderabad"
print(student)
