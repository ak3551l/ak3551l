class Student():
    def __init__(self, first, last, house):

        if not :
            raise ValueError("Missing Name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")

        self.first = first
        self.last = last
        self.house = house


def main():
    student = get_student()
    print(f"{student.first} {student.last} from {student.house}")



def get_student():


    first = input("First: ")
    last = input("Last: ")
    house = input("House: ")
    student = Student(first, last, house)
    return student

if __name__ == "__main__":
    main()
