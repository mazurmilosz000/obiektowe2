import time

class Time_iterator():
    def __init__(self):
        self.start_time = time.time()

    def __iter__(self):
         return self

    def __next__(self):
        return time.time() - self.start_time


def time_generator():
    start_time = time.time()
    while True:
        yield time.time() - start_time


if __name__ == '__main__':

    # time1 = Time_iterator()
    # for i in time1:
    #     print(i)

    for i in time_generator():
        print(i)


