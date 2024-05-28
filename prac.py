import sys

try:
    print("my name is", sys.argv[1])
except IndexError:
    print("Too many arguments")
