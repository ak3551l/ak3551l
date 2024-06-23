import sys

try:
    print("My name is", sys.argv[1])
except IndexError:
    print("Too few arguments.")
