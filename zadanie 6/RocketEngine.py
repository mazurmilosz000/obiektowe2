class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power, working=False):
        self.name = name
        self.power = power
        self.working = working
        RocketEngine.count += 1

    def start(self):
        if not self.working:
            RocketEngine.all_power += self.power
            self.working = True

    def stop(self):
        if self.working:
            RocketEngine.all_power -= self.power
            self.working = False

    def __str__(self):
        return f"nazwa to: {self.name}\nmoc wynosi: {self.power}\nsilnik pracuje: {self.working}"

    def __del__(self):
        if self.working:
            RocketEngine.all_power -= self.power
        RocketEngine.count -= 1

    @staticmethod
    def status():
        print(f"ilosc silnikow: {RocketEngine.count}\ncalkowita moc silnikow: {RocketEngine.all_power}")




