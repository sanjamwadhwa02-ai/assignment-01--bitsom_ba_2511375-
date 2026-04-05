

with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: Modules organize code.\n")

print("Lines appended.")

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("\nFile Content:\n")

for i in range(len(lines)):
    print(f"{i+1}. {lines[i].strip()}")

print("\nTotal lines:", len(lines))



keyword = input("\nEnter keyword to search: ").lower()

found = False

print("\nMatching lines:")

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")