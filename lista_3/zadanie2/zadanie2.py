import math

def calkowite(a=1):
    while True:
        yield a
        a +=1

def kwadrat(n=1):
    for i in calkowite(n):
        yield i ** 2

# for a in calkowite():
#     print(a)

def select(n, item):
    list = []
    for _ in range(n):
        list.append(next(item))
    return list

def pitagoras():
    a = next(calkowite())**2 - next(kwadrat())
    b = 2 * next(calkowite()) * math.sqrt(next(kwadrat()))
    c = next(calkowite())**2 + next(kwadrat())
    for _ in calkowite():
        yield (a, b, c)


def pita():
    for n in calkowite():
        for m in kwadrat():
            a = m**2 - n
            b = 2 * m * math.sqrt(n)
            c = m**2 + n

            yield (a, b, c)


def jak():
    for m in calkowite():
        yield m


# for a in calkowite():
#     print(a)

print(select(5, kwadrat()))
print(select(15, calkowite()))
print(select(15, pita()))

