orders = [
    {"order_id": 1, "customer": "Rahul", "amount": 2500},
    {"order_id": 2, "customer": "Sneha", "amount": 1800},
    {"order_id": 3, "customer": "Rahul", "amount": 3200},
    {"order_id": 4, "customer": "Amit", "amount": 1500}
]

spending = {}
orders_count = {}

for order in orders:
    c = order["customer"]

    spending[c] = spending.get(c, 0) + order["amount"]
    orders_count[c] = orders_count.get(c, 0) + 1

print("Spending:", spending)
print("Orders:", orders_count)

top_customer = max(spending, key=spending.get)
print("Top Customer:", top_customer)