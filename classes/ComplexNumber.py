class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.image = imag

    def displayComplex(self):
        print(self.real, "+", self.image, "j")

    def __str__(self):
        if self.image >= 0:
            return f'{self.real}+{self.image}j'
        else:
            return f'{self.real}{self.image}j'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        real = self.real*other.real-self.image*other.image
        image = self.real * other.image - self.image * other.real
        return ComplexNumber(real, image)


a = ComplexNumber(1, 2)
a.displayComplex()
print("a =", a)
b = ComplexNumber(1, 1)
print("b =", b)
print("a+b =", a+b)
print("a-b =", a+b)
print("a*b =", a*b)
