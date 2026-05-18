languages = ["Python\n", "Java\n", "C++\n"]

with open("data.txt", "w") as file:
    file.writelines(languages)

with open("data.txt", "a") as file:
    file.write("Priya\n")