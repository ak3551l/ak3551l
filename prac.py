import sys

if len(sys.argv) < 2:
    sys.exit("Few arguments")
elif len(sys.argv) > 2:
    sys.exit("Many arguments")

print("Hello, " + sys.argv[1])
