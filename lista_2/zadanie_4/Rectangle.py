class Rectangle():
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return f'length: {self.length}\nheight: {self.height}\narea: {self.area}'

    def __repr__(self):
        return f'length: {self.length}, height: {self.height}'

class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def area(self):
        return 2*super().area() + 2*self.height*self.width + 2*self.length*self.width

    def volume(self):
        return super().area() * self.width

    def __str__(self):
        return super().__str__() + f'\nvolume: {self.volume}'

    def __repr__(self):
        return super().__repr__() + f', width: {self.width}'

class Except(Exception):
    pass

class InvalidData(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return f'Invalid data: {self.msg}'
