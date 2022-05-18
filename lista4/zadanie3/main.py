from Temperature import *
from random import sample

if __name__ == '__main__':
    list1 = []
    list1 += (Celsius(x) for x in sample(range(-100, 100), 4))
    list1 += (Fahrenheit(x) for x in sample(range(-200, 200), 4))
    list1 += (Kelvin(x) for x in sample(range(-400, 400), 4))

    # (?) do poprawy
    # for el in list1:
    #     if el.above_freezing:
    #         print(f"{el} - above zero")
    #     else:
    #         print(el)

    f_list = (t.convert_to_fahrenheit() for t in list1)
    c_list = (t.convert_to_celsius() for t in list1)
    k_list = (t.convert_to_kelvin() for t in list1)

    for el in f_list:
        print(el)

# dokonczyc, dodac funkcje wyswietlajaca temperature