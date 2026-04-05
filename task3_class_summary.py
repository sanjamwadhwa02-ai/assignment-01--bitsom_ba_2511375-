# Class Data
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("-" * 40)

pass_count = 0
fail_count = 0
total_avg_sum = 0

topper_name = ""
topper_avg = 0

for student in class_data:
    name = student[0]
    marks = student[1]
    
    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg
    
  
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
    
  
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
  
    print(f"{name:<18} | {avg:>7} | {status}")

class_avg = round(total_avg_sum / len(class_data), 2)

print("\nSummary:")
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)
print("Class Topper:", topper_name, "-", topper_avg)
print("Class Average:", class_avg)