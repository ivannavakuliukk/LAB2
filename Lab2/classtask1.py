class Rectangle:
    def __init__(self, width = 1, length = 1):
        self.__width = width
        self.__length = length
    def set_width_and_length(self, width, length):
        if not isinstance(self.__width, int) or not isinstance(self.__length, int):
            raise TypeError
        if width < 1 or width > 21 or length < 1 or length > 21:
            raise ValueError
        self.__width = width
        self.__length = length

    def get_width_and_length(self):
        return self.__width, self.__length

    def get_area(self):
        return self.__width * self.__length

    def get__perimeter(self):
        return (self.__length + self.__width) * 2


a = Rectangle()
a.set_width_and_length(22, 5)
print(a.get_width_and_length())
print(f"perimeter: {a.get_area()}, area: {a.get__perimeter()}")