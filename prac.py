import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments.")

for arg in sys.argv:
    print("my name is", arg)
