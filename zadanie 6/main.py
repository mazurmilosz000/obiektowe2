from RocketEngine import *

if __name__ == '__main__':
    print("-------------Statek stoi, ma dwa male silniki:------------------- \n")
    small_engine1 = RocketEngine('maly silnik 1', 50)
    small_engine2 = RocketEngine('maly silnik 2', 50)

    print("stan statku: \n")
    RocketEngine.status()

    print("\nStan silnikow:")
    print(f"\nsilnik 1: \n{small_engine1}\n\nsilnik 2: \n{small_engine2}\n\n")

    print("----------Statek startuje:---------- \n")
    small_engine1.start()
    small_engine2.start()

    print("\nStan silnikow:")
    print(f"\nsilnik 1: \n{small_engine1}\n\nsilnik 2: \n{small_engine2}\n\n")

    print("stan statku: \n")
    RocketEngine.status()

    print("\n----------Statek wytwarza dwa srednie silniki i rozpedza sie:---------- \n")
    medium_engine1 = RocketEngine('sredni silnik 1', 500)
    medium_engine2 = RocketEngine('sredni silnik 2', 500)

    print("\n----------Statek wylacza male silniki i wlacza srednie:---------- \n")

    small_engine1.stop()
    small_engine2.stop()
    medium_engine1.start()
    medium_engine2.start()

    print("\nStan silnikow:")
    print(f"\nsilnik 1: \n{small_engine1}\n\nsilnik 2: \n{small_engine2}\n\nsilnik 3: \n{medium_engine1}\n\nsilnik 4: "
          f"\n{medium_engine2}\n\n")

    print("stan statku: \n")
    RocketEngine.status()

    print("\n----------Statek wytwarza dwa duze silniki i wchodzi w hiperpredkosc:---------- \n")
    main_engine1 = RocketEngine('glowny silnik 1', 400000)
    main_engine2 = RocketEngine('glowny silnik 2', 400000)

    medium_engine1.stop()
    medium_engine2.stop()
    main_engine1.start()
    main_engine2.start()
    print(f"\nsilnik 1: \n{small_engine1}\n\nsilnik 2: \n{small_engine2}\n\nsilnik 3: \n{medium_engine1}\n\nsilnik 4: "
          f"\n{medium_engine2}\n\nsilnik 5: \n{main_engine1}\n\nsilnik 6: \n{main_engine2}\n\n")

    print("stan statku: \n")
    RocketEngine.status()

    print("\n----------Statek wychodzi z hiperpredkosci i zwalnia:---------- \n")
    del main_engine1
    del main_engine2
    medium_engine1.start()
    medium_engine2.start()

    print("stan statku: \n")
    RocketEngine.status()

    print("\n----------Statek zwalnia i manewruje:---------- \n")
    del medium_engine1
    del medium_engine2
    small_engine1.start()
    small_engine2.start()

    print("stan statku: \n")
    RocketEngine.status()

    print("\n----------Statek cumuje w porcie:---------- \n")
    del small_engine1
    del small_engine2

    print("stan statku: \n")
    RocketEngine.status()



