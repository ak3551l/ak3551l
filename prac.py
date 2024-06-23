students = []

with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}.")

for student in sorted(students):
    print(student)

print(students)
