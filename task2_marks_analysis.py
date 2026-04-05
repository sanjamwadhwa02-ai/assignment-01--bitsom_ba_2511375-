
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Student:", student_name)
print("=" * 30)

for i in range(len(subjects)):
    m = marks[i]
    
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(subjects[i], ":", m, "Grade:", grade)

total = sum(marks)
average = round(total / len(marks), 2)

print("\nTotal:", total)
print("Average:", average)

max_marks = max(marks)
min_marks = min(marks)

print("Highest:", subjects[marks.index(max_marks)], "-", max_marks)
print("Lowest:", subjects[marks.index(min_marks)], "-", min_marks)

count = 0

while True:
    subject = input("\nEnter subject (or 'done'): ")
    
    if subject == "done":
        break
    
    m = input("Enter marks: ")
    
    if not m.isdigit():
        print("Invalid input!")
        continue
    
    m = int(m)
    
    if m < 0 or m > 100:
        print("Marks must be 0-100")
        continue
    
    subjects.append(subject)
    marks.append(m)
    count += 1

new_avg = round(sum(marks) / len(marks), 2)

print("\nNew subjects added:", count)
print("Updated average:", new_avg)