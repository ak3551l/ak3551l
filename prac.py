import sys

if len(sys.argv) < 2:
    print("Too few arguments")
if len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("my name is", sys.argv[1])
