import unittest


class DistanceTest(unittest.TestCase):
    def test_4(self):
        self.assertEqual(distance("abc", "cba"), 2)

    def test_5(self):
        self.assertEqual(distance("Течение", "Течении"), 1)


def distance(x: str, y: str):
    pass


if __name__ == "__main__":
    unittest.main()
    