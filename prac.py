from calc import square

def main():
    test_squared()

def test_squared():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
