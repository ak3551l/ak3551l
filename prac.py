name = input("Enter your name: ")

if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"
    print("Hello,", name)
