from datetime import date

class Note:
    count = 0
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.today = date.today()
        Note.count += 1
        self.ID = Note.count


    def match(self, str):
        if str == self.text or str == self.tag:
            return True
        else:
            return False

class Notebook(Note):
    list = []
    def __init__(self, text, tag):
        super().__init__(text, tag)
        self.notes = list

    def new_note(self, new_n):
        self.notes.append(Note(new_n, self.tag))







