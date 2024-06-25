import re

email = input("What's your email?: ").rstrip()

if re.search(".+@.+", email):
    print("Valid")

else:
    print("Invalid")
