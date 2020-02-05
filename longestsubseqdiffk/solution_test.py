import unittest
from .solution import find


class SolutionTestCase(unittest.TestCase):
    def test_find(self):
        self.assertEqual(4, find("afcbedg", 2))
        self.assertEqual(7, find("geeksforgeeks", 3))


if __name__ == '__main__':
    unittest.main()
