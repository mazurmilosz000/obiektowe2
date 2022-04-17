class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age > 130:
            raise ValueError('age must be a number between 0 and 130')
        self._age = new_age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            raise ValueError('name must be more than 3 characters long')
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        if len(new_surname) < 3:
            raise ValueError('surname must be more than 3 characters long')
        self._surname = new_surname

    def __str__(self):
        return f'name: {self.name}\nsurname: {self.surname}\nage: {self.age}'

class Student(Person):
    def __init__(self, name, surname, age, field_of_study):
        super().__init__(name, surname, age)
        self.field_of_study = field_of_study
        self.student_book = {}

    def add_mark(self, subject, mark):
        if mark < 2 or mark > 5:
            raise ValueError('mark must be a number between 2 and 5')
        self.student_book[subject] = mark

    def __str__(self):
        return super().__str__() + f'\nfield of study: {self.field_of_study}\n student book: {self.student_book}'

class Employee(Person):
    def __init__(self, name, surname, age, job_title):
        super().__init__(name, surname, age)
        self.job_title = job_title
        self.skills = []

    def add_skills(self, new_skill):
        self.skills.append(new_skill)

    def __str__(self):
        return super().__str__() + f'\njob title: {self.job_title}\n skills: {self.skills}'



