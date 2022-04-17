import random

class Die:
    def __init__(self, sides, value=None):
        self._sides = sides
        self._value = value

    def roll(self):
        self._value = random.randrange(1,self._sides+1,1)

    def get_sides(self):
        return self._sides

    def get_value(self):
        return self._value

class Player():
    throw = None
    total_points = 0

def game():
    die1 = Die(6)
    die2 = Die(6)
    player = Player()
    computer = Player()

    while player.total_points < 21:
        die1.roll()
        computer.throw = die1.get_value()
        computer.total_points += computer.throw
        print("Czy chcesz kontynuowac rzucanie (tak/nie): ")
        answer = input()
        if answer == 'nie' or player.total_points > 21:
            break
        elif answer == 'tak':
            die2.roll()
            player.throw = die2.get_value()
            player.total_points += player.throw
            print(f"Suma twoich punktow to:{player.total_points}")
        else:
            print("wpisz tak lub nie!")

    print(f"\nSuma twoich punktow to: {player.total_points}\n suma punktow komputera to: {computer.total_points}")

    is_winner: bool
    if player.total_points > 21:
        is_winner = False
    elif computer.total_points > 21:
        is_winner = True
    elif player.total_points > computer.total_points:
        is_winner = True
    else:
        is_winner = False

    if is_winner:
        print("Wygrales gre")
    else:
        print("Niestety przegrales")


if __name__ == '__main__':
    game()