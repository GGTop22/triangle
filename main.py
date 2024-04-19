from triangle import Triangle

# Пример использования класса Triangle
try:
    triangle = Triangle(3, 4, 5)
    print("Периметр треугольника:", triangle.perimeter())
    print("Площадь треугольника:", triangle.area())
except ValueError as e:
    print(e)
