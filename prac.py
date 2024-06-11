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

    def charm(self):
        match self.patronus:
            case "Stag":
                return "STAG"
            case "Otter":
                return "OTTER"
            case "Jack Russell Terrier":
                return "RUSSELL"
            case _:
                return "MAGIC"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm)



def get_student():


    name = input("Name: ")
    house = input("House: ")
    patronus  = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
