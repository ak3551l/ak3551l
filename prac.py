class Student():
    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError("Missing Name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        print(f"{student.name} from {student.house}")



def main():
    student = get_student()
    



def get_student():


    name = input("Name: ")
    house = input("House: ")
    patronus  = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
