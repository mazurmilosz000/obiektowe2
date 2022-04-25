class Pupil():
    def __init__(self):
        self.marks = {}
    def add_marks(self):
        x =input('x: ')
        y =input('y: ')
        self.marks[x] = y

class uczen(Pupil):
    pass

if __name__ == '__main__':

    pupil1 = Pupil()
    pupil1.add_marks()
    uczen1 = uczen()
    print(pupil1.marks)
    print(uczen1.marks)