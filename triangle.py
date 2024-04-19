class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами невозможен")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
