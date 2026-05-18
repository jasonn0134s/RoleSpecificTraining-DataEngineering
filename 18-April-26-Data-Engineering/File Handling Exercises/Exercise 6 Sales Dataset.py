import csv

with open("sales.csv", "r") as f:
    data = list(csv.DictReader(f))

total = 0
for s in data:
    total += int(s["quantity"]) * int(s["price"])

print("Total revenue:", total)

qty = {}
for s in data:
    p = s["product"]
    qty[p] = qty.get(p, 0) + int(s["quantity"])

print(qty)

top = max(qty, key=qty.get)
print("Top product:", top)

revenue = {}
for s in data:
    p = s["product"]
    revenue[p] = revenue.get(p, 0) + int(s["quantity"]) * int(s["price"])

print(revenue)

for p in revenue:
    if revenue[p] > 50000:
        print(p)