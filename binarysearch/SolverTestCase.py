import unittest
from .Solver import Solver


class SolverTestCase(unittest.TestCase):
    def test_find(self):
        self.assertEqual(False, Solver.find([], 10))
        self.assertEqual(False, Solver.find([11, 5, 10], 12))
        self.assertEqual(True, Solver.find([11, 5, 10], 10))


if __name__ == '__main__':
    unittest.main()
