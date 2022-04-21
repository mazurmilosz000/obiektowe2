import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(username+password)
        self.is_logged = False

    def _encrypt_password(self, password):
        # hash_password = hashlib.sha256(password.encode('utf-8'))
        # return hash_password
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, given_password):
        return self.password == self._encrypt_password(given_password)


class AuthenticException(Exception):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


class PermissionError(Exception):
    pass


class NotPermittedError(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class PasswordTooShort(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class IncorrectPassword(AuthenticException):
    pass


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, user, password):

        if user not in self.users:
            if len(password) > 7:
                self.users[user] = User(user,password)
            else:
                raise PasswordTooShort("password should contain at least 7 characters")
        else:
            raise UsernameAlreadyExists("username already exists!")

    def login(self, username, password):

        if username in self.users:
            if password == self.users[username].check_password(password):
                self.users[username].is_logged = True
                return True
            else:
                raise IncorrectPassword("incorrect password!")
        else:
            raise IncorrectUsername("user doesn't exist!")

    def is_logged_in(self, username):
        if username not in self.users:
            raise IncorrectUsername("user doesn't exist!")
        else:
            return self.users[username].is_logged


class Authorizor:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions[permission] = set()
        else:
            raise PermissionError('permission already exist')

    def permit_user(self, username, permission):
        if permission not in self.permissions:
            raise PermissionError("Permission doesn't exist")
        if username not in self.authenticator.users:
            raise IncorrectUsername("User doesn't exist")
        self.permissions[permission].add(username)

    def check_permission(self, username, permission):
        if permission in self.permissions:
            if username in self.authenticator.users:
                if username in self.permissions[permission]:
                    return True
                else:
                    raise NotPermittedError('user has not permission')
            else:
                raise NotLoggedError("user doesn't exist")
        else:
            raise PermissionError("permission doesn't exist")


auth = Authenticator()
auth.add_user('user', 'password123')
auth.add_user('user1', 'password123')

authorizor = Authorizor(auth)

authorizor.add_permission('testing')
authorizor.add_permission('changing')

authorizor.permit_user('user', 'testing')
authorizor.permit_user('user1', 'changing')







