# Store student data in a dictionary
# Format: { "Name": marks }
students = {}

# Input data for 5 students
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Print all student data
print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Calculate class average
total_marks = sum(students.values())
average_marks = total_marks / len(students)

print("\nTopper:", topper, "with marks:", top_marks)
print("Class Average:", average_marks)

# Assign grades
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print(name, "->", grade)