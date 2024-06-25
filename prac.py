import re

email = input("What's your email?: ").rstrip()

if re.search(r"\w+@\w+\.(com|edu|gov|net|gmail)$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")
