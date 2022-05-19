from Students import Pupil, Student

if __name__ == "__main__":

    pupil1 = Pupil('janusz', 'kowalski')
    pupil1.complete_marks()
    print(pupil1)
    print(pupil1.marks)
    student1 = Student('kacper', 'nowak')
    student1.complete_marks()
    student1.complete_weights()
    print(student1)
    print(student1.marks)
    print(student1.weights)
