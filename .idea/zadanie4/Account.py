class Account:
    def __init__(self,balance):
        self._balance = balance

    def pay(self,value):
        self._balance += value

    def take(self,value):
        if self._balance >=value:
            self._balance -= value
        else:
            print("Nie masz wystarczajacej ilosci srodkow na koncie")

    def show_balance(self):
        return self._balance

    def __str__(self):
        return 'Stan Twojego konta wynosi: ' + str(self._balance) + ' zl'
