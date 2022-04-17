from minesweeper import saper


def sapper():
    ms = saper()
    ms.a = ms.get_number(8, 30, "Podaj pierwszy wymiar planszy z zakresu ")
    ms.b = ms.get_number(8, 24, "Podaj drugi wymiar planszy z zakresu ")
    ms.mines_count = ms.get_number(10, (ms.a-1)*(ms.b-1), "Podaj liczbe min z zakresu ")

    ms.mines_position = ms.lay_mines()
    number = ms.number_of_neighboring_mines((7,7))


    print(ms.mines_position)
    print(number)
    print(ms.create_board())
  #  print(ms.get_number(7,14, "Podaj liczby z zakresu"))

sapper()

