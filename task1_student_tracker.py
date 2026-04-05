
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    
    name = student["name"].strip().title()
    
    roll = int(student["roll"])
    marks = list(map(int, student["marks_str"].split(", ")))
    
    is_valid = all(word.isalpha() for word in name.split())
    
    if is_valid:
        print(f"{name} → ✓ Valid name")
    else:
        print(f"{name} → ✗ Invalid name")
    
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)
    print()

for student in cleaned_students:
    if student["roll"] == 103:
        name = student["name"]
        print("Special Output for Roll 103:")
        print("UPPERCASE :", name.upper())
        print("lowercase :", name.lower())