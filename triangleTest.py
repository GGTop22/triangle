import unittest

from triangle import Triangle


class TriangleTest(unittest.TestCase):
    def test_perimetr(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(12, t.perimeter())
        t = Triangle(100, 100, 100)
        self.assertEqual(300, t.perimeter())

    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(6, t.area())
        t = Triangle(8, 15, 17)
        self.assertEqual(60, t.area())

    def test_existOrNot(self):
        t = Triangle(3, 4, 5)
        self.assertRaises(ValueError, Triangle, 3, 4, 50)
        self.assertRaises(ValueError, Triangle, 1, 3, 1)
        self.assertRaises(ValueError, Triangle, 100, 49, 48)
        self.assertRaises(ValueError, Triangle, 3, 4, -2)
        self.assertRaises(ValueError, Triangle, 0, 0, 0)
        self.assertRaises(ValueError, Triangle, 0, 2, 2)
        self.assertRaises(ValueError, Triangle, 0, 2, 3)


if __name__ == '__main__':
    unittest.main()
