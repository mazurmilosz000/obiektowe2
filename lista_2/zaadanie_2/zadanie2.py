from figure_module import *

if __name__ == "__main__":
    circle1 = Circle('red', False, 8)
    print(circle1)
    print(circle1.__repr__())
    rectangle1 = Rectangle('blue', True, 2,3)
    print(rectangle1)
    print(rectangle1.__repr__())
    print(rectangle1.__dict__())
