import re

email = input("What's your email?: ").rstrip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.edu$", email):
    print("Valid")

else:
    print("Invalid")
