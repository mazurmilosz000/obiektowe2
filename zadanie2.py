import random

class Coin:
    def __init__(self):
        self.side = None
        self.value = None

    def throw(self):
        self.side = random.choice(['orzel', 'reszka'])

    def show_side(self):
        return self.side


def throw_15():
    coin_list = []
    for _ in range(15):
        coin1 = Coin()
        coin1.throw()
        coin_list.append(coin1)

    coin_counter={"orzel": 0, "reszka": 0}
    for coin in coin_list:
        if coin.side == "orzel":
            coin_counter["orzel"] += 1
        else:
            coin_counter["reszka"] += 1

        print(coin.side)

    print(f"wynik: orzel = {coin_counter['orzel']}, reszka = {coin_counter['reszka']} ")

def game():
    balance = {'win': 0, 'lose': 0}
    coin_list = []
    one = Coin()
    one.value = 1
    two = Coin()
    two.value = 2
    five = Coin()
    five.value = 5
    coin_list.append(one)
    coin_list.append(two)
    coin_list.append(five)

    for i in range(100):
        count = 0
        while count < 20:
            for coin in coin_list:
                coin.throw()
                if coin.side == 'orzel':
                    count += coin.value
        if count == 20:
            balance['win'] += 1
        else:
            balance['lose'] += 1

    print(f"wynik 100 gier to: {balance['win']} zwyciestw oraz {balance['lose']} porazek")




if __name__ == '__main__':

    throw_15()
    game()


