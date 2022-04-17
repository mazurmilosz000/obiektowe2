from Note import *

if __name__ == '__main__':
    note1 = Note('123',  3)
    print(note1.today)
    print(note1.ID)

    notebook1 = Notebook('123', 3)
    notebook1.new_note(note1)