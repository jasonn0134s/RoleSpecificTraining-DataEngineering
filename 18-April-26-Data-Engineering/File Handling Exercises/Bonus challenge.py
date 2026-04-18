import csv

with open("sales.csv", "r") as f:
    data = list(csv.DictReader(f))

qty = {}
revenue = {}

for s in data:
    p = s["product"]
    q = int(s["quantity"])
    price = int(s["price"])

    qty[p] = qty.get(p, 0) + q
    revenue[p] = revenue.get(p, 0) + q * price

for p in qty:
    print(p, "→ Qty:", qty[p], "Revenue:", revenue[p])