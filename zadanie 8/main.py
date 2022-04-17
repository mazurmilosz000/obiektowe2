from pet import *

if __name__ == '__main__':

    pet1 = Pet()

    while not pet1.name:
        pet_name = input("Podaj imie swojego zwierzaka: ")
        if pet_name.isalpha():
            pet1.name = pet_name
        else:
            print("Imie twojego zwierzaka musi skladac sie z samych lietr!")

    print("""
    ___________________MENU__________________
    1. Rozmawiaj
    2. Nakarm
    3. Baw sie
    4. Wyswietl stan zwierzaka
    5. Koniec gry
    
    
    """)

    while True:
        choice = int(input("Co chcesz teraz zrobic?: "))
        if choice == 1:
            pet1.talk()
        elif choice == 2:
            food = input(f"Jak duzo {pet1.name} ma zjesc?: ")
            if food.isdigit():
                pet1.eat(int(food))
            else:
                pet1.eat()
        elif choice == 3:
            fun = input(f"Jak duzo {pet1.name} ma sie bawic?: ")
            if fun.isdigit():
                pet1.play(int(fun))
            else:
                pet1.play()
        elif choice == 4:
            print(pet1)
        elif choice == 5:
            break
        else:
            print("Podales zla wartosc!")


