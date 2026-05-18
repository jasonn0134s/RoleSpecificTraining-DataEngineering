sales = [
    {"product":"Laptop","qty":5},
    {"product":"Mouse","qty":20},
    {"product":"Laptop","qty":3},
    {"product":"Keyboard","qty":10}
]

total = {}

for item in sales:
    p = item["product"]
    total[p] = total.get(p, 0) + item["qty"]

print(total)

highest = max(total, key=total.get)
print("Highest:", highest)