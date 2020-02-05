import unittest
from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(5, solve(4, {1, 2}))
        self.assertEqual(4, solve(5, {1, 3}))


if __name__ == '__main__':
    unittest.main()
