from authorization_system import *

class Editor:
    def __init__(self):
        self.username = None
        self.options = {"a": self.login,
                        "b": self.test,
                        "c": self.change,
                        "d": self.quit}


    def login(self):
        try:
            username = input("username: ")
            password = input("password: ")
            auth.login(username, password)
            self.username = self.username
        except AuthenticException as e:
            print(e)

    def is_permitted(self, permission):
        try:
            authorizor.check_permission(self.username, permission)
        except NotLoggedError as e:
            print(e)
        except PermissionError as e:
            print(e)


    def test(self):
        self.is_permitted("testing")

    def change(self):
        self.is_permitted("changing")

    def quit(self):
        print('quit')
        exit()

    def run(self):
        while True:
            print("""
            a. login
            b. test
            c. change
            d. quit""")
            option = input('select option: ')
            self.options[option]()
