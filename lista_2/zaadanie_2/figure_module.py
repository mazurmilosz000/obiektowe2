import math

class Figure:
    def __init__(self, colour = None, is_filled = False):
        self.colour = colour
        self.is_filled = is_filled

    def __str__(self):
        return f"colour:  {self.colour}, is filled: {self.is_filled}"



    def __repr__(self):
        return f"colour: {self.colour}, is filled: {self.is_filled}"

class Circle(Figure):
    def __init__(self,colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = new_radius

    @property
    def area(self):
        return 3.14 * self.radius**2

    @property
    def perimeter(self):
        return 2 * 3.14 * self.radius

    @property
    def diameter(self):
        return 2 * self.radius

    def __str__(self):
        return super().__str__() + f', radius: {self.radius}, area: {self.area}, perimeter {self.perimeter},' \
                                   f'diameter: {self.diameter}'

    def __repr__(self):
        return super().__repr__()

class Rectangle(Figure):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError("width cannot be negative")
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height < 0:
            raise ValueError("height cannot be negative")
        self._height = new_height

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * self.height + 2 * self.width

    @property
    def diagonal(self):
        return math.sqrt(self.height**2 + self.width**2)

    def __str__(self):
        return super().__str__() + f', width: {self.width}, height: {self.height}, area: {self.area}, perimeter {self.perimeter},' \
                            f'diagonal: {self.diagonal}'

    def __repr__(self):
        return super().__repr__()

    def __dict__(self):
        return {
            "width": self.width,
            "height": self.height,
            "area": self.area,
            "perimeter": self.perimeter,
            "diagonal": self.diagonal
        }







