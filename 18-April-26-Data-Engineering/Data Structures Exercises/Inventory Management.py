inventory = {
    "laptop":10,
    "mouse":25,
    "keyboard":15
}

inventory["monitor"] = 8
inventory["laptop"] -= 2

for item, qty in inventory.items():
    if qty < 10:
        print(item)