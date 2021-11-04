from math import gcd


class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError
        self._numerator = numerator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError
        if not denominator:
            raise ValueError("division by zero")
        self._denominator = denominator

    def __str__(self):
        divisor = gcd(self.numerator, self.denominator)
        return f'{self.numerator//divisor}/{self.denominator//divisor}'

    def floating(self):
        divisor = gcd(self.numerator, self.denominator)
        return (self.numerator//divisor)/(self.denominator//divisor)


num1 = Rational(2,8)
print(num1)
print(num1.floating())