class Pet:
    def __init__(self):
        self.name = ""
        self.hunger = 0
        self.tiredness = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pet_name):
        if not pet_name or len(pet_name) >= 3:
            self._name = pet_name
        else:
            print("Podano imie zwierzaka, ktore nie spelnia warunkow")

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        count = self.hunger + self.tiredness
        if count < 5:
            return "szczesliwy"
        elif count < 11:
            return "zadowolony"
        elif count < 16:
            return "podenerwowany"
        else:
            return "wsciekly"

    def talk(self):
        print(f"{self.name} jest {self.mood}")
        self._passage_of_time()

    def eat(self, food=4):
        self.hunger -= food
        self._passage_of_time()

    def play(self, fun=4):
        self.tiredness -= fun
        self._passage_of_time()

    def __str__(self):
        return f"Twoj zwierzak ma na imie: {self.name}\njego poziom glodu wynosi: {self.hunger}\njego poziom zmeczenia" \
               f"wynosi: {self.tiredness}\n"





