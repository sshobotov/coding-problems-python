import unittest

from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(220, solve([60, 100, 120], [10, 20, 30], 50))


if __name__ == '__main__':
    unittest.main()
