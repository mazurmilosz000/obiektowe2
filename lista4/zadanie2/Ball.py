import time
import random

class Ball:
    def __init__(self, number, ballast=None):
        self.number = number
        self.ballast = ballast


class LotteryMachine:
    def __init__(self):
        self.ball_list = [Ball(x) for x in range(49)]
        self.active = False

    def init_ball_ballast(self):
        for x in range(6):
            self.ball_list[43+x].ballast = True


    def __draw(self):
        while self.active:
            # j = random.randrange(49)
            # d = random.randrange(49)
            # temp = self.ball_list[j]
            # self.ball_list[j] = self.ball_list[d]
            # self.ball_list[d] = temp
            # time.sleep(10)
            print("aktywne")
        else:
            print("nie")


    def start(self):
        self.active = True
        LotteryMachine.__draw(self)

    def stop(self):
        self.active = False
        i = 0
        while i < 6:
            yield self.ball_list[i]
            i += 1



if __name__ == '__main__':

    machine = LotteryMachine()
    machine.init_ball_ballast()


    print(time.time_ns())
    machine.start()
    machine.stop()
    # machine_list = list(machine.stop())
    # for l in machine_list:
    #     print(l.number)
    for balls in machine.ball_list:
        print(balls.number)
