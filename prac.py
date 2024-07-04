name = input("Name: ")

with open("friends.csv", "a") as file:
    write = file.write(f"{name}\n")
