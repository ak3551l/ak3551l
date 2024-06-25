import re

email = input("What's your email? ")

if re.search(r"\w+@\w+\.(com|edu|gov|net|gmail)$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")

