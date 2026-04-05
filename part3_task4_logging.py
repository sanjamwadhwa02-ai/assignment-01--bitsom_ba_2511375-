import requests
from datetime import datetime


def log_error(function_name, error_type, message):
    with open("error_log.txt", "a", encoding="utf-8") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"[{time}] ERROR in {function_name}: {error_type} — {message}\n"
        file.write(log)




try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError:
    print("Connection error triggered.")
    log_error("fetch_products", "ConnectionError", "No connection could be made")

try:
    url = "https://dummyjson.com/products/999"
    response = requests.get(url, timeout=5)
    
    if response.status_code != 200:
        print("HTTP error triggered.")
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")

except requests.exceptions.ConnectionError:
    log_error("lookup_product", "ConnectionError", "No connection")
except requests.exceptions.Timeout:
    log_error("lookup_product", "Timeout", "Request timed out")




print("\nError Log Content:\n")

with open("error_log.txt", "r", encoding="utf-8") as file:
    print(file.read())