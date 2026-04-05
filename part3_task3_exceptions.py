import requests


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("Safe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))



def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\nReading existing file:")
print(read_file_safe("python_notes.txt"))

print("\nReading missing file:")
read_file_safe("ghost_file.txt")


url = "https://dummyjson.com/products?limit=5"

try:
    response = requests.get(url, timeout=5)
    data = response.json()
    
    print("\nProducts fetched:")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)


url_post = "https://dummyjson.com/products/add"

try:
    response = requests.post(url_post, json={"title": "Test Product"}, timeout=5)
    print("\nPOST Response:", response.json())

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)



while True:
    user_input = input("\nEnter product ID (1–100) or 'quit': ")
    
    if user_input.lower() == "quit":
        break
    
    if not user_input.isdigit():
        print("Invalid input! Enter a number.")
        continue
    
    product_id = int(user_input)
    
    if product_id < 1 or product_id > 100:
        print("Enter ID between 1 and 100.")
        continue
    
    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            data = response.json()
            print("Product:", data["title"], "-", data["price"])
    
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)