def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generator(n):
    n_range = range(2, n+1)
    for i in n_range:
        if czy_pierwsza(i) == True:
            yield i


def to_file():
    with open("pierwsze.txt", "w") as f:
        for i in generator(1000):
            f.write(f'{i}\n')

if __name__ == '__main__':
    to_file()





