# Task 1
with open('website_visits.txt','r') as f:
    visits=[line.strip() for line in f.readlines()]
    print("Website Visited")


# Task 2
print("All Visitors:",visits)



# Task 3
total_visits=len(visits)
print(f"Total Visits: {total_visits}")



# Task 4
unique_visitors=set(visits)
print(f"Unique Visitors: {unique_visitors}")



# Task 5
visit_counts={}
for name in visits:
    visit_counts[name]=visit_counts.get(name,0) + 1
print("Visit Counts:",visit_counts)


# Task 6
most_frequent_visitor=max(visit_counts,key=visit_counts.get)
print(f"Most Frequent Visitor: {most_frequent_visitor}")



import json

# Task 7
with open('products.json','r') as f:
    data=json.load(f)
    products_list=data['products']
    print("Products Loaded")


# Task 8
for p in products_list:
    print(f"Product: {p['name']}, Price: {p['price']}")



# Task 9
product_dict = {p['product_id']: {"name": p['name'], "price": p['price']} for p in products_list}
print("Product Dictionary:", product_dict)



# Task 10
most_expensive=max(products_list, key=lambda x: x['price'])
print(f"Most Expensive: {most_expensive['name']}")


# Task 11
least_expensive=min(products_list, key=lambda x: x['price'])
print(f"Least Expensive: {least_expensive['name']}")



import csv

# Task 12
orders=[]
with open('orders.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        row['product_id']=int(row['product_id'])
        row['quantity']=int(row['quantity'])
        orders.append(row)
    print("csv Orders read")


# Task 13
for order in orders:
    print(order)



# Task 14
qty_per_product={}
for o in orders:
    pid=o['product_id']
    qty_per_product[pid]=qty_per_product.get(pid,0)+o['quantity']
print("Quantity per product:",qty_per_product)



# Task 15
orders_per_customer={}
for o in orders:
    cust=o['customer']
    orders_per_customer[cust]=orders_per_customer.get(cust,0)+1
print("Orders per customer:",orders_per_customer)


# Task 16
for o in orders:
    price=product_dict[o['product_id']]['price']
    o['order_revenue']=price * o['quantity']
    print(o)



# Task 17
total_revenue=sum(o['order_revenue'] for o in orders)
print(f"Total Revenue: {total_revenue}")



# Task 18
rev_per_product={}
for o in orders:
    p_name=product_dict[o['product_id']]['name']
    rev_per_product[p_name]=rev_per_product.get(p_name, 0)+o['order_revenue']
print("Revenue per product:",rev_per_product)


# Task 19
top_selling_product=max(rev_per_product,key=rev_per_product.get)
print(f"Top Selling Product: {top_selling_product}")




# Task 20
customer_spending={}
for o in orders:
    cust=o['customer']
    customer_spending[cust]=customer_spending.get(cust,0)+o['order_revenue']
print("Customer Spending:",customer_spending)


# Task 21
top_customer=max(customer_spending,key=customer_spending.get)
print(f"Top Customer: {top_customer}")



# Task 22
big_spenders=[cust for cust,spend in customer_spending.items() if spend>50000]
print("Big Spenders:",big_spenders)


import json
import csv



# Functions (Tasks 23-28)

def load_visits(filepath):
    with open(filepath,'r') as f:
        return [line.strip() for line in f.readlines()]

def load_products(filepath):
    with open(filepath,'r') as f:
        data=json.load(f)
        return {p['product_id']: {"name": p['name'], "price": p['price']} for p in data['products']}

def load_orders(filepath):
    orders_list=[]
    with open(filepath,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            row['product_id']=int(row['product_id'])
            row['quantity']=int(row['quantity'])
            orders_list.append(row)
    return orders_list

def calc_product_revenue(orders_list,p_dict):
    rev={}
    for o in orders_list:
        p_info=p_dict[o['product_id']]
        name=p_info['name']
        rev[name]=rev.get(name, 0)+(p_info['price']*o['quantity'])
    return rev

def calc_customer_spending(orders_list,p_dict):
    spending={}
    for o in orders_list:
        cust=o['customer']
        p_price=p_dict[o['product_id']]['price']
        spending[cust]=spending.get(cust,0)+(p_price*o['quantity'])
    return spending

def find_top_customer(spending_dict):
    return max(spending_dict,key=spending_dict.get)

visits=load_visits('website_visits.txt')
product_dict=load_products('products.json')
orders=load_orders('orders.csv')

unique_visitors=set(visits)
visit_counts={}
for v in visits:
    visit_counts[v]=visit_counts.get(v,0)   +1
product_revenue=calc_product_revenue(orders, product_dict)
product_revenue_tuples = [(prod, rev) for prod, rev in product_revenue.items()]
print("Product Revenue (tuples):", product_revenue_tuples)
customer_spending=calc_customer_spending(orders, product_dict)
top_cust=find_top_customer(customer_spending)
total_rev=sum(product_revenue.values())

#   TASK 28
with open('sales_report.txt', 'w', encoding='utf-8') as f:
    f.write("E-Commerce Sales Report\n")
    f.write(f"Total Website Visits: {len(visits)}\n")
    f.write(f"Unique Visitors: {len(unique_visitors)}\n")
    f.write(f"Total Revenue: ₹{total_rev}\n\n")
    f.write(f"Top Customer: {top_cust}\n")
    f.write("\nProduct Sales:\n")
    for prod, rev in sorted(product_revenue.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{prod:<10} : ₹{rev}\n")

# Task 29: Visited but never ordered
ordering_customers = {o['customer'] for o in orders}
visited_no_order = unique_visitors - ordering_customers
print(f"Visitors who never ordered: {', '.join(visited_no_order) if visited_no_order else 'None'}")

# Task 30: Ordered but visited <= 1 time
ordered_rare_visitors = [cust for cust in ordering_customers if visit_counts.get(cust, 0) <= 1]

print(f"Customers who visited <=1 time: {', '.join(ordered_rare_visitors) if ordered_rare_visitors else 'None'}")