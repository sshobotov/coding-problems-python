import unittest
from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual([(0, 0)], solve(1))
        self.assertEqual(None, solve(3))
        self.assertEqual([(0, 1), (1, 3), (2, 0), (3, 2)], solve(4))
        self.assertEqual([(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)], solve(8))


if __name__ == '__main__':
    unittest.main()
