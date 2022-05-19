import time
from datetime import datetime, timedelta
import random


class Ball:
    def __init__(self, number, ballast=False):
        self.number = number
        self.ballast = ballast


class LotteryMachine:
    def __init__(self):
        self.ball_list = [Ball(x) for x in range(49)]
        self.active = False

    def init_ball_ballast(self):
        for x in range(6):
            self.ball_list[43+x].ballast = True

    def __draw(self, exist_time):
        end_time = datetime.now() + timedelta(seconds=exist_time)
        while datetime.now() < end_time:
            # zamiana miejsc dwoch losowo wybranych kul
            j = random.randrange(49)
            d = random.randrange(49)
            temp = self.ball_list[j]
            self.ball_list[j] = self.ball_list[d]
            self.ball_list[d] = temp
            # przesuwanie kul oszukanych w gore
            for element in self.ball_list:
                if element.ballast:
                    index = self.ball_list.index(element)
                    prev_index = index-1
                    prev_element = self.ball_list[prev_index]
                    self.ball_list[prev_index], self.ball_list[index] = element, prev_element
            time.sleep(0.01)
        else:
            self.stop()
            print("losowanie dobieglo konca!")

    def start(self, exist_time):
        LotteryMachine.__draw(self, exist_time)

    def stop(self):
        i = 0
        while i < 6:
            yield self.ball_list[i]
            i += 1
