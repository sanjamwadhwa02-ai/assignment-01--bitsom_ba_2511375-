import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

inventory_backup = copy.deepcopy(inventory)

inventory["Paneer Tikka"]["stock"] = 5

print("After manual change:")
print("Inventory:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

inventory = copy.deepcopy(inventory_backup)

print("\nInventory restored.\n")


for item in cart:
    name = item["item"]
    qty = item["quantity"]
    
    if name in inventory:
        stock = inventory[name]["stock"]
        
        if stock >= qty:
            inventory[name]["stock"] -= qty
        else:
            print(f"⚠ Not enough stock for {name}")
            inventory[name]["stock"] = 0

print("\nReorder Alerts:")

for item in inventory:
    stock = inventory[item]["stock"]
    reorder = inventory[item]["reorder_level"]
    
    if stock <= reorder:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder})")

print("\nFinal Inventory (Updated):")
print(inventory)

print("\nInventory Backup (Original):")
print(inventory_backup)