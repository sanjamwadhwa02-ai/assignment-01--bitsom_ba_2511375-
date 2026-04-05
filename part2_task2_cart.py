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


cart = []

def show_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)

def add_item(name, qty):
    if name not in menu:
        print(name, "not found in menu!")
        return
    
    if not menu[name]["available"]:
        print(name, "is unavailable!")
        return
    
        for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            print(name, "quantity updated!")
            return
    
        cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })
    print(name, "added to cart!")


def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            print(name, "removed from cart!")
            return
    print(name, "not in cart!")



add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)
show_cart()

add_item("Mystery Burger", 1)
show_cart()

add_item("Chicken Wings", 1)
show_cart()

remove_item("Gulab Jamun")
show_cart()


print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price
    
    print(f"{item['item']:<18} x{item['quantity']}   ₹{total_price:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:             ₹{subtotal:.2f}")
print(f"GST (5%):             ₹{gst:.2f}")
print(f"Total Payable:        ₹{total:.2f}")
print("===================================")