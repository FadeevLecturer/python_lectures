import unittest
from math import prod, pow 


class ArithmeticMeanTest(unittest.TestCase):
    def test_1(self):
        x = [1, 2, 3]
        self.assertAlmostEqual(arithmetic_mean(x), 2)
        
    def test_2(self):
        self.assertIsNone(arithmetic_mean([]), None)


class GeometricMeanTest(unittest.TestCase):
    def test_1(self):
        x = [1, 2, 3]
        self.assertAlmostEqual(geometric_mean(x), pow(6, 1/3))
        
    def test_2(self):
        self.assertIsNone(geometric_mean([]), None)


class HarmonicMeanTest(unittest.TestCase):
    def test_1(self):
        x = [1, 2, 3]
        self.assertAlmostEqual(harmonic_mean(x), 18/11)
        
    def test_2(self):
        self.assertIsNone(harmonic_mean([]), None)


def arithmetic_mean(data: list[float]):
    pass
    
def geometric_mean(data: list[float]):
    pass
    
def harmonic_mean(data: list[float]):
    pass


if __name__ == "__main__":
    unittest.main()
