email = input("What's your email?: ").rstrip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")

else:
    print("Invalid")
