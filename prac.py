def main():
    x = int(input("Enter value of x: "))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")

def is_even(n):
    return True if n % 2 == 0 else False


main()
