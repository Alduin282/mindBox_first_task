import unittest
import math
from circle import Circle
from triangle import Triangle
from areaCalculator import AreaCalculator

class TestCirle(unittest.TestCase):
    def setUp(self) -> None:
        self.Circle = Circle(4)

    def test_area(self):
        self.assertAlmostEqual(self.Circle.area, math.pi * 4 ** 2)
        self.assertEqual(self.Circle.radius,4)
    
        self.Circle.radius = 5
        self.assertEqual(self.Circle.radius,5)
        self.assertAlmostEqual(self.Circle.area, math.pi * 5** 2)
    
        self.Circle.radius = 5.5
        self.assertEqual(self.Circle.radius,5.5)
        self.assertAlmostEqual(self.Circle.area, math.pi * 5.5** 2)
        
    
    def test_radius_not_positive_number(self):
        with self.assertRaises(ValueError):
            self.Circle.radius = 0
        with self.assertRaises(ValueError):
            self.Circle.radius = -5504545
        with self.assertRaises(ValueError):
            self.Circle.radius = ")))"
        with self.assertRaises(ValueError):
            self.Circle.radius = True
        with self.assertRaises(ValueError):
            self.Circle.radius= "1"
        with self.assertRaises(ValueError):
            self.Circle.radius=ValueError
        with self.assertRaises(ValueError):
            self.Circle.radius="0"

class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle(5,4,3)

    def test_area(self):
        self.assertEqual(self.triangle.area,6.0)

    def test_right(self):
        self.assertTrue(self.triangle.is_right)

    def test_change_sides1(self):
        self.triangle.side_lengths = [5,5,5]
        self.assertAlmostEqual(self.triangle.area,10.825317547305483)
        self.assertFalse(self.triangle.is_right)

    def test_change_sides2(self):
        self.triangle.change_sides(6,10,6)
        self.assertAlmostEqual(self.triangle.area,16.583123951777)
        self.assertFalse(self.triangle.is_right)

    def test_change_sides_float(self):
        self.triangle.change_sides(6.555,7.595,8.12)
        self.assertAlmostEqual(self.triangle.area,23.330451254315676)

    def test_bad_sides_in_change_sides(self):
        with self.assertRaises(ValueError):
            self.triangle.change_sides(0,1,1)
        with self.assertRaises(ValueError):
            self.triangle.change_sides(1,-1,1)
        with self.assertRaises(ValueError):
            self.triangle.change_sides(1,1,-1)
        with self.assertRaises(ValueError):
            self.triangle.change_sides(True,True,True)
        with self.assertRaises(ValueError):
            self.triangle.change_sides("1","1","1")
        with self.assertRaises(ValueError):
            self.triangle.change_sides(ValueError,1,1)
    
    def test_bad_sides_in_setter(self):
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = [0,1,1]
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = [1,-1,1]
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = [1,1,-1]
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = [True,True,True]
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = ["1","1","1"]
        with self.assertRaises(ValueError):
            self.triangle.side_lengths = [ValueError,1,1]

class TestFigureArea(unittest.TestCase):
    def setUp(self) -> None:
        self.area_calculator1 = AreaCalculator(Circle(5))
        self.area_calculator2 = AreaCalculator(Triangle(4,3,5))
    
    def test_area(self):
        self.assertEqual(self.area_calculator1.area,78.53981633974483)
        self.assertEqual(self.area_calculator2.area,6.0)
        self.assertEqual(AreaCalculator.get_area(Circle(5)),78.53981633974483)
        self.assertEqual(AreaCalculator.get_area(Triangle(4,3,5)),6.0)
    
    def test_type_figure(self):
        with self.assertRaises(ValueError):
            k = AreaCalculator(True)
        with self.assertRaises(ValueError):
            c = AreaCalculator.get_area(True)
        with self.assertRaises(ValueError):
            k = AreaCalculator(ValueError)
        with self.assertRaises(ValueError):
            c = AreaCalculator.get_area(ValueError)
    



    
        
if __name__ == "__main__":
    unittest.main()