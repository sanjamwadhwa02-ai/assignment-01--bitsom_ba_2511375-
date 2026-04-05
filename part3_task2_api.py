import requests



url = "https://dummyjson.com/products?limit=20"

response = requests.get(url)
data = response.json()

products = data["products"]

print("\nID | Title                     | Category     | Price   | Rating")
print("-" * 70)

for p in products:
    print(f"{p['id']:<3}| {p['title'][:25]:<25}| {p['category']:<12}| ${p['price']:<7}| {p['rating']}")


filtered = []

for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)

filtered.sort(key=lambda x: x["price"], reverse=True)

print("\nFiltered (Rating ≥ 4.5, sorted by price):")

for p in filtered:
    print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")


url2 = "https://dummyjson.com/products/category/laptops"

response2 = requests.get(url2)
data2 = response2.json()

print("\nLaptops:")

for p in data2["products"]:
    print(f"{p['title']} - ${p['price']}")


url3 = "https://dummyjson.com/products/add"

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response3 = requests.post(url3, json=new_product)

print("\nPOST Response:")
print(response3.json())