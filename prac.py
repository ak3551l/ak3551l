file = open("names.txt", "r")
lines = file.readlines()

for line in lines:
    print("Hello, ",line.lstrip())

file.close()
