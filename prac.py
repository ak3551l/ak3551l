import re

email = input("What's your email?: ").rstrip()

if re.search(r"\w+@\w+\.edu$", email):
    print("Valid")

else:
    print("Invalid")
