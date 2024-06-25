name = input("Name: ")

file = open("names.csv", "a")
file.write(f"{name}\n")
file.close()



