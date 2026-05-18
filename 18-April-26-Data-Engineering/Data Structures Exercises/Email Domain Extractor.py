emails = [
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@gmail.com",
    "user4@outlook.com"
]
domain_count = {}
for email in emails:
    domain = email.split("@")[1]
    domain_count[domain] = domain_count.get(domain, 0) + 1
print(domain_count)
