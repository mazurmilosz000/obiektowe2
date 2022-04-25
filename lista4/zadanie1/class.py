class Pupil():
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.marks = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            raise ValueError("za krotkie imie")
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        if len(new_surname) < 3:
            raise ValueError("za krotkie nazwisko")
        self._surname - new_surname

    def complete_marks(self):
        marks = (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6)
        while True:
            answer = input("Czy chcesz dodac przedmiot? (tak/nie): ")
            if answer == 'tak':
                subject = input("Wpisz nazwe przedmiotu: ")
                mark = float(input("Wpisz ocene: "))
                if mark in marks:
                    self.marks[subject] = mark
                else:
                    raise ValueError("Podales zla ocene")
            elif answer == 'nie':
                break
            else:
                raise ValueError("Podales zla odpowiedz")

    def mean(self):
        marks = self.marks.values()
        count = 0
        for mark in marks:
            count += mark

        average = count/len(marks)
        format_average = "{:.2f}".format(average)
        return format_average

    def __str__(self):
        return f"Imie: {self.name}\nNazwisko: {self.surname}\nSrednia ocen: {self.mean()}"

class Student(Pupil):
    def __init__(self,name,surname):
        super(Student, self).__init__(name,surname)


if __name__ == "__main__":

    pupil1 = Pupil('janusz', 'kowalski')
    pupil1.complete_marks()
    print(pupil1)
    print(pupil1.marks)
    student1 = Student('kacper', 'nowak')
    print(student1.marks)