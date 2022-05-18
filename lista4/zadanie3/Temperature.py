from abc import ABC, abstractmethod


class Temperature(ABC):

    @abstractmethod
    def __init__(self, temperature):
        self._temperature = temperature

    def __str__(self):
        return f"{self._temperature} degrees {self.__class__.__name__}"

    def __repr__(self):
        return f"ClassName({self.__class__.__name__})"

    def above_freezing(self):
        return self._temperature > 0

    @abstractmethod
    def convert_to_fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_celsius(self):
        pass

    @abstractmethod
    def convert_to_kelvin(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        pass

    @temperature.setter
    @abstractmethod
    def temperature(self, temp):
        pass


class Fahrenheit(Temperature):

    def __init__(self, temperature):
        self._temperature = temperature

    def convert_to_fahrenheit(self):
        return self

    def convert_to_celsius(self):
        return Celsius((self._temperature-32) * 5/9)

    def convert_to_kelvin(self):
        return Kelvin((self._temperature + 459.67) * 5/9)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature


class Celsius(Temperature):

    def __init__(self, temperature):
        self._temperature = temperature

    def convert_to_fahrenheit(self):
        return Fahrenheit((self._temperature * 9/5) + 32)

    def convert_to_celsius(self):
        return self

    def convert_to_kelvin(self):
        return Kelvin(self._temperature + 273.15)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature


class Kelvin(Temperature):

    def __init__(self, temperature):
        self._temperature = temperature

    def convert_to_fahrenheit(self):
        return Fahrenheit(self._temperature * 9/5 - 459.67)

    def convert_to_celsius(self):
        return Celsius(self._temperature - 273.16)

    def convert_to_kelvin(self):
        return self

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
