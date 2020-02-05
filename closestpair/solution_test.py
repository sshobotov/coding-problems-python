import unittest
from .solution import find


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(((2, 3), (3, 4)), find([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)])[1])
        self.assertEqual(((5, 1), (6, 1)), find([(2, 3), (12, 30), (40, 50), (5, 1), (6, 1), (3, 4)])[1])


if __name__ == '__main__':
    unittest.main()
