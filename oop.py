def main():
    name = get_name()
    house = get_house()

    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()







def main():
    name, house = get_student()
    print(f"{name} from {house}")




def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__  == "__main__":
    main()









def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")





def get_student():

    student['name'] = input("Name: ")
    student['house'] = input("House: ")
    return student




class Student():
    ...

def main():
    student = get_student()

    print(f"{student.name} from {student.house}")

def get_student():

    # Creating a data type Student() and an Object
    student = Student()

    # Giving name attribute and house attribute to the student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()








class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():


    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()







if not name:
            raise ValueError("Missing Name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")

        self.name = name
        self.house = house









