from Note import *

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }
    def show_menu(self):
        print("""
        ------MENU------
        1. Pokaz notatki
        2. Szukaj notatek
        3. Dodaj notatke
        4. Zmodyfikuj notatke
        5. Wyjdz
        """)

    def run(self):
        while True:
            self.show_menu()
            key = input('Wybierz opcje: ')
            choice = self.options.get(key)
            if choice:
                choice()
            else:
                print('Nie ma takiej metody')

    def show_notes(self, notes = None):
        if notes is None:
            notes = self.notebook.notes

        if len(notes) == 0:
            print("Nie ma zadnych notatek")

        for note in notes:
            print(f"Id notatki: {note.id}, etykieta notatki: {note.tag}, zawartosc notatki: {note.text}")
            print("-"*20)

    def search_notes(self):
        phrase = input("Wpisz szukany tekst: ")
        matched = self.notebook.search(phrase)
        self.show_notes(matched)

    def add_note(self):
        tag = input("Podaj etykiete notatki: ")
        text = input("Podaj tekst notatki: ")
        self.notebook.new_note(Note(text, tag))

    def modify_note(self):
        id = int(input("Podaj id notatki: "))
        choice = int(input("""
        Co chcesz edytowac:
        1. etykiete
        2. tekst notatki
        """))
        if choice == 1:
            self.notebook.modify_tag(id)
        elif choice == 2:
            self.notebook.modify_text(id)
        else:
            print("Nie ma takiej opcji")

    def quit(self):
        exit()


if __name__ == "__main__":

    menu = Menu()
    menu.run()


