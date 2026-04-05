sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}


print("Revenue per day:")

best_day = ""
max_revenue = 0

for date in sales_log:
    total = 0
    
    for order in sales_log[date]:
        total += order["total"]
    
    print(date, ":", total)
    
    if total > max_revenue:
        max_revenue = total
        best_day = date

print("\nBest-selling day:", best_day, "-", max_revenue)



item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

most_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_item = item

print("\nMost ordered item:", most_item, "-", max_count, "times")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue per day:")

best_day = ""
max_revenue = 0

for date in sales_log:
    total = sum(order["total"] for order in sales_log[date])
    
    print(date, ":", total)
    
    if total > max_revenue:
        max_revenue = total
        best_day = date

print("\nNew Best-selling day:", best_day, "-", max_revenue)

print("\nAll Orders:\n")

all_orders = []

for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

for i, (date, order) in enumerate(all_orders, start=1):
    items = ", ".join(order["items"])
    
    print(f"{i}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")