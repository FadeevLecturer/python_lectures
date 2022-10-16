import unittest
from numbers import Number

class DistanceTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(distance(42, 13), 29)
        
    def test_2(self):
        self.assertAlmostEqual(distance(3.14, 2.71), 0.43000000000000016)

    def test_3(self):
        self.assertAlmostEqual(distance(1+2j, 3+4j), 2.8284271247461903)

    def test_4(self):
        self.assertEqual(distance("abc", "cba"), 2)

    def test_5(self):
        self.assertEqual(distance("Течение", "Течении"), 1)


        


def distance(x, y):
    pass

if __name__ == "__main__":
    unittest.main()
    