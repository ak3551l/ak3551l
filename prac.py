import sys

if len(sys.argv) < 2:
    print("Few arguments")
elif len(sys.argv) > 2:
    print("Many arguments")

print("Hello, " + sys.argv[1])
