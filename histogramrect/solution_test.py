import unittest
from .solution import solve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(0, solve([], 0))
        self.assertEqual(5, solve([5], 1))
        self.assertEqual(12, solve([6, 2, 5, 4, 5, 1, 6], 7))
        self.assertEqual(15, solve([1, 2, 3, 4, 5, 3, 3, 2], 8))


if __name__ == '__main__':
    unittest.main()
