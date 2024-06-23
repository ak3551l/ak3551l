with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}.")
