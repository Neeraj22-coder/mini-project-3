subjects = ("Python", "Maths", "DBMS")
students = {}
student_ids = []
n = int(input("Enter number of students: "))
for i in range(n):
    sid = input("\nEnter Student ID: ")
    while sid in students:
        print("ID already exists!")
        sid = input("Enter another ID: ")
    name = input("Enter Name: ")
    marks = []
    for sub in subjects:
        m = int(input(sub + " marks: "))
        while m < 0 or m > 100:
            print("Enter marks between 0 and 100")
            m = int(input(sub + " marks: "))
        marks.append(m)
    total = sum(marks)
    avg = total / 3

    if avg >= 75:
        result = "Distinction"
    elif avg >= 40:
        result = "Pass"
    else:
        result = "Fail"
    students[sid] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "result": result
    }
    student_ids.append(sid)
print("\n--- STUDENT REPORT ---")
for sid in students:
    print("\nID:", sid)
    print("Name:", students[sid]["name"])
    print("Marks:", students[sid]["marks"])
    print("Total:", students[sid]["total"])
    print("Average:", students[sid]["average"])
    print("Result:", students[sid]["result"])
sid = input("\nEnter ID to search: ")
if sid in students:
    print("Student Found")
    print(students[sid])
else:
    print("Student Not Found")
print("\nFirst two IDs:", student_ids[:2])
if len(student_ids) > 0:
    print("Python Marks:",
          students[student_ids[0]]["marks"][0])

sid = input("\nEnter ID to update: ")
if sid in students:
    sub = input("Enter subject (Python/Maths/DBMS): ")
    if sub in subjects:
        pos = subjects.index(sub)
        m = int(input("Enter new marks: "))
        while m < 0 or m > 100:
            print("Enter marks between 0 and 100")
            m = int(input("Enter new marks: "))
        students[sid]["marks"][pos] = m
        marks = students[sid]["marks"]
        total = sum(marks)
        avg = total / 3
        if avg >= 75:
            result = "Distinction"
        elif avg >= 40:
            result = "Pass"
        else:
            result = "Fail"
        students[sid]["total"] = total
        students[sid]["average"] = avg
        students[sid]["result"] = result
        print("Marks Updated!")
    else:
        print("Invalid Subject")
else:
    print("Student Not Found")

all_passed = set()
student_sets = {}
for sid in students:
    passed = set()
    for i in range(3):
        if students[sid]["marks"][i] >= 40:
            passed.add(subjects[i])
    student_sets[sid] = passed
    all_passed.update(passed)
print("\nSubjects passed by at least one student:")
print(all_passed)

if len(student_ids) >= 2:
    a = student_sets[student_ids[0]]
    b = student_sets[student_ids[1]]
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference:", a - b)
averages = []
for sid in students:
    averages.append(students[sid]["average"])
print("\n--- CLASS SUMMARY ---")
print("Total Students:", len(students))
print("Class Average:", sum(averages) / len(averages))
print("Highest Average:", max(averages))
print("Lowest Average:", min(averages))
print("Unique Subjects:", set(subjects))