import re

name = input("Enter your name: ")

matches = re.search(r"^(.+), ?(.+)$", name)

if matches:

    name = matches.group(2) + " " + matches.group(1)

    print("Hello,", name)
