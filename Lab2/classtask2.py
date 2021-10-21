from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        if not isinstance(numerator, int):
            raise TypeError
        if not denominator:
            raise ValueError("division by zero")
        self.__numerator = numerator
        self.__denominator = denominator
        divisor = gcd(self.__numerator, self.__denominator)
        self.__numerator//=divisor
        self.__denominator//=divisor

    def trad(self):
        return f'{self.__numerator}/{self.__denominator}'

    def floating(self):
        return self.__numerator/self.__denominator


num1 = Rational(5,10)
print(num1.trad())
print(num1.floating())