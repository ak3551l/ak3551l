def main():
    x = int(input("Enter value of x: "))
    if x % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
