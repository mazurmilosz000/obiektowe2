class TV:
    def __init__(self):
        self._channel = None
        self._volume = 0


    @property
    def channel(self):
        return self._channel

    @property
    def volume(self):
        return self._volume

    @channel.setter
    def channel(self, channel_number):
        if channel_number < 1 or channel_number > 99:
            print("Zly zakres")
            self._channel = self._channel
        else:
            self._channel = channel_number

    @volume.setter
    def volume(self, volume):
        if volume == '+':
            if self._volume < 10:
                self._volume +=1
            else:
                self._volume = 10
        elif volume == '-':
            if self._volume > 1:
                self._volume -=1
            else:
                self._volume = 0
        else:
            print("zle!!")

if __name__ == '__main__':

    tv = TV()
    print("MENU:\n\nZeby zmienic kanal wcisnij 1.\nZeby zmienic poziom glosnosci wybierz 2.\nZeby wyswietlic poziom "
          "glosnosci wybierz 3.\nZeby wyswietlic aktualny program wybierz 4.\nZeby wylaczyc telewizor wybierz 5\n")
    print("_______________TELEWIZOR______________")
    tv.channel = 99
    print(tv.channel)
    print(tv.volume)
    while True:
        value = int(input("Co chcesz zrobic?: "))
        if value == 1:
            print("Podaj kanal z zakresu 1-99")
            channel_input = int(input())
            tv.channel = channel_input
        elif value == 2:
            print("Wpisz '+' zeby zwiekszyc glosnosc lub '-' zeby zmniejszyc")
            volume_input = input()
            tv.volume = volume_input
        elif value == 3:
            print(tv.volume)
        elif value == 4:
            print(tv.channel)
        elif value == 5:
            break
        else:
            print("Podales zla wartosc!")

