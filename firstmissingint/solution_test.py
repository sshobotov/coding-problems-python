import unittest
from .solution import find


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2, find([3, 4, -1, 1], 4))
        self.assertEqual(3, find([1, 2, 0], 3))
        self.assertIsNone(find([3, 2, 1], 3))
        self.assertIsNone(find([], 0))


if __name__ == '__main__':
    unittest.main()
