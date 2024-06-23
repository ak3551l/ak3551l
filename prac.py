students = []

with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {'name': name, 'house': house}
        students.append(student)

def get_house(student):
    return student['house']


# Sorted according to value of house name.
for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")


