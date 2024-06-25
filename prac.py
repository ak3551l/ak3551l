import re

name = input("Enter your name: ")

matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last, first = name.split(",")
    name = f"{first} {last}"
    print("Hello,", name)
