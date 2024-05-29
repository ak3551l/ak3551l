import sys

if len(sys.argv) < 2:
    sys.exit("Few arguments")

for arg in sys.argv:
    print("Hello, " + arg)
