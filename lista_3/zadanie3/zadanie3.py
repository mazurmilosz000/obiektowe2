class Fibo():
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.n -= 1
        return self.a




def generator_fibo(n, a = 0, b = 1):
    for i in range(n):
        a, b = b, a+b
        yield a


def function():
    list = [x for x in generator_fibo(100000)]
    fibo_a = list[-1]
    fibo_b = list[-2]
    str_fibo_a = str(fibo_a)
    print(f'F100000 ma: {len(str_fibo_a)} cyfr')

    for x in generator_fibo(20, fibo_a, fibo_b):
        yield x


if __name__ == '__main__':

    for i in Fibo(19):
        print(i)

    for x in generator_fibo(19):
        print(x)

    with open("fibo.txt", "w") as f1:
        for i in function():
            f1.write(f'{i}\n\n\n')