from datetime import date

class Note:
    count = 0
    def __init__(self,text, tag):
        self.text = text
        self.tag = tag
        self.date = date.today()
        Note.count += 1
        self.id = Note.count

    def match(self, text):
        return self.text.find(text) != -1 or self.tag.find(text) != -1

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, notebook):
        self.notes.append(notebook)

    def modify_text(self, id):
       if id > len(self.notes) or id < len(self.notes):
           raise Exception('nie ma notatki o takim id')
       for note in self.notes:
           if note.id == id:
               note.text = input("Podaj nowy tekst notatki: ")

    def modify_tag(self, id):
        if id > len(self.notes) or id < len(self.notes):
            raise Exception('nie ma notatki o takim id')
        for note in self.notes:
            if note.id == id:
                note.tag = input("Podaj nowy tag notatki: ")

    # def search(self, phrase):
    #     matched_list = []
    #     for note in self.notes:
    #         if note.text.find(phrase) != -1 or note.tag.find(phrase) != -1:
    #             matched_list.append(note)
    #     return matched_list

    def search(self,phrase):
        matched_list = []
        for note in self.notes:
            if note.match(phrase):
                matched_list.append(note)
        return matched_list








