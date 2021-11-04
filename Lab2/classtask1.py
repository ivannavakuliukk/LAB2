class Rectangle:
    def __init__(self, width = 1, length = 1):
        self.width = width
        self.length = length

    def __str__(self):
        return f'area: {self.get_area()}, perimeter: {self.get_perimeter()}'

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if not isinstance(length, int):
            raise TypeError
        if not 0 < length < 20:
            raise ValueError
        self._length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError
        if not 0 < width < 20:
            raise ValueError
        self._width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width


a = Rectangle(5, 4)
b = Rectangle()
print(a)
print(b)