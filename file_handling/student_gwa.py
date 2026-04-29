students = []
with open('students.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        name = parts[0].strip()
        gwa = float(parts[1].strip())
        students.append((name, gwa))

if students:
    highest_student = max(students, key=lambda x: x[0])
    print(f"Student with Highest GWA:")
    print(f"Name: {highest_student[0]}")
    print(f"GWA: {highest_student[1]}")
else:
    print("No students found in file")
