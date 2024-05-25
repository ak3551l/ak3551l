def main():
    length = int(input("Enter the value: "))
    print_square(length)

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()
main()
