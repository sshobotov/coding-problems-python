import unittest
from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(15, solve(4))


if __name__ == '__main__':
    unittest.main()
