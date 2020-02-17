import unittest
from .Solver import Solver


class SolverTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(9, Solver.find([30, 9, 30, 25, 25, 30, 25]))


if __name__ == '__main__':
    unittest.main()
