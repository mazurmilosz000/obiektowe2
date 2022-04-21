

def gen_time(start, stop, leap):
    n_start = time(start)
    n_stop = time(stop)
    n_leap = time(leap)
    while n_start < n_stop:
        yield tuple(n_start)
        n_start += n_leap


def time(tuple):
    return tuple[0] * 3600 + tuple[1] * 60 + tuple[2]


def tuple(time):
    return time//3600, (time % 3600//60), time % 60

for x in gen_time((8 , 10, 00) , (10 , 50, 15) , (0, 15, 12)):
    print(x)