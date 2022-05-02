from Ball import *


class LottoPresenter:
    def __init__(self):
        pass

    def main(self):
        machine = LotteryMachine()
        print("Witam wszystkich w wielkim losowaniu!")
        print("-"*30)
        draw_time = int(input("\n\nProsze podaj czas trwania losowania w sekundach: "))
        if draw_time < 1:
            raise ValueError("Czas trwania losowania nie moze byc krotszy niz sekunda")
        machine.start(draw_time)
        machine_list = list(machine.stop())
        for el in machine_list:
            print(el.number)


if __name__ == '__main__':
    presenter = LottoPresenter()
    presenter.main()


