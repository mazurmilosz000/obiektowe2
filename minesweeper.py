import random


class saper:
    def __init__(self):
        self.a = None  # plansza a * b (wartosc a)
        self.b = None  # plansza a * b (wartosc b)
        self.mines_count = None  # liczba min
        self.mines_position = []  # lista pozycji min

    def get_number(self, a, b, text):
        number = 0
        while number < a or number > b:
            number = int(input(f"{text} od {a} do {b}: "))
            if number < a or number > b:
                print("Podales liczbe ze zlego zakresu!")
            else:
                return number

    def lay_mines(self):
        position = []
        for i in range(self.mines_count):
            x = random.randint(0, self.a - 1)
            y = random.randint(0, self.b - 1)
            if (x, y) not in self.mines_position:
                position.append((x, y))

        return position

    def number_of_neighboring_mines(self, coordinates):
        count = 0
        x, y = coordinates
        for i in range(-1,2):
            for j in range(-1,2):
                if(x+i, y+j) in self.mines_position:
                    count += 1

        return count

    def create_board(self):
        array = []
        for i in range(self.b):
            array.append([])
            for j in range(self.a):
                if (i, j) in self.mines_position:
                    array[i].append(9)
                else:
                    array[i].append(self.number_of_neighboring_mines((i,j)))

        return array

    # def reveal_fields(self, field):
    #     x,y = field
    #     if

