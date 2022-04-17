class Smartphone:
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def set_manufacturer(self, new_manufacturer):
        self.__manufacturer = new_manufacturer

    def set_model(self, new_model):
        self.__model = new_model

    def set_price(self, new_price):
        self.__price = new_price

    def print_manufacturer(self):
        print(f"producent to: {self.__manufacturer}")

    def print_model(self):
        print(f"model to: {self.__model}")

    def print_price(self):
        print(f"cena to: {self.__price}")

    def __str__(self):
        return f"producent: {self.__manufacturer}\nmodel: {self.__model}\ncena: {self.__price}"
