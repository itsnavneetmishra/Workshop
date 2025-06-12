import math 

class Fraction:
    def __init__(self , numerator,  denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = math.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __eq__(self, other):
        return (self.numerator == other.numerator and self.denominator == other.denominator)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    
    print("f1:", f1)
    print("f2:", f2)
    print("f1 + f2 =", f1 + f2)
    print("f1 == f2?", f1 == f2)
    print("f1 < f2?", f1 < f2)
    print("f1 >= f2?", f1 >= f2)