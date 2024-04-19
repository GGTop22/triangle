class TriangleTester:
    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a


a, b, c = 3, 4, 5
if TriangleTester.is_triangle(a, b, c):
    print("Треугольник с такими сторонами существует")
else:
    print("Треугольник с такими сторонами не существует")

