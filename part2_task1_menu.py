menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

categories = []
for item in menu:
    cat = menu[item]["category"]
    if cat not in categories:
        categories.append(cat)

for cat in categories:
    print(f"\n===== {cat} =====")
    
    for item in menu:
        if menu[item]["category"] == cat:
            price = menu[item]["price"]
            status = "Available" if menu[item]["available"] else "Unavailable"
            
            print(f"{item:<15} ₹{price:.2f}   [{status}]")

total_items = len(menu)

available_items = 0
for item in menu:
    if menu[item]["available"]:
        available_items += 1

max_price = 0
max_item = ""

for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        max_item = item

print("\nItems under ₹150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, "-", menu[item]["price"])

print("\nSummary:")
print("Total items:", total_items)
print("Available items:", available_items)
print("Most expensive item:", max_item, "-", max_price)