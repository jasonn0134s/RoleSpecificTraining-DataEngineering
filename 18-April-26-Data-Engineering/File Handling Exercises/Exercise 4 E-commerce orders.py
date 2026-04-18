import json

with open("orders.json", "r") as f:
    data = json.load(f)

orders = data["orders"]

print(orders)

total = sum(o["amount"] for o in orders)
print("Total revenue:", total)

spend = {}
for o in orders:
    c = o["customer"]
    spend[c] = spend.get(c, 0) + o["amount"]

print(spend)

top = max(spend, key=spend.get)
print("Top customer:", top)

count = {}
for o in orders:
    c = o["customer"]
    count[c] = count.get(c, 0) + 1

print(count)