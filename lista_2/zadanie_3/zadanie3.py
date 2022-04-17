from Person import *

if __name__ == "__main__":

    student1 = Student('Janusz', 'Kowalski', 23, 'informatyka')
    print(student1)
    student1.add_mark('programowanie w pythonie', 5)
    student1.add_mark('grafika komputerowa',3)
    print(student1)

    print('-'*50)
    employee1 = Employee('Marek', 'Nowak', 46, 'dekarz')
    print(employee1)
    employee1.add_skills('praca na wysokosci')
    employee1.add_skills('koncentracja')
    print(employee1)


