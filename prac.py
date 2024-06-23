with open("names.txt", "r") as file:

    for line in sorted(file):
        print("Hello, ", line.rstrip())
