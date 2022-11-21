import unittest
from math import nan, isnan, inf


class FilterMissingValuesTest(unittest.TestCase):
    def test_1(self):
        x = [None, 3.14, None, None, 2.71, 1.41, None]
        y = [3.14, 2.71, 1.41]
        self.assertEqual(filter_missed_values(x), y)
        
    def test_2(self):
        x = [inf/inf, 3.14, nan, float("nan"), 2.71, 1.41, inf - inf]
        y = [3.14, 2.71, 1.41]
        self.assertEqual(filter_missed_values(x), y)


def filter_missed_values(data: list[float|None]):
    pass
    
if __name__ == "__main__":
    unittest.main()
