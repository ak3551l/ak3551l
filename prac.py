class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():

    student = Student()
    name = input("Name: ")
    house = input("House: ")
    return student

if __name__ == "__main__":
    main()
