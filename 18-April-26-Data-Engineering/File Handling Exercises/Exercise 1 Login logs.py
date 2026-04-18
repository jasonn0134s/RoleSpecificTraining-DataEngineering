with open("logins.txt", "r") as f:
    names = f.read().splitlines()

print("All names:")
for name in names:
    print(name)

print("Total login records:", len(names))

count = {}
for name in names:
    count[name] = count.get(name, 0) + 1

print("Login counts:", count)

most_user = max(count, key=count.get)
print("User with most logins:", most_user)

print("Unique users:", set(names))