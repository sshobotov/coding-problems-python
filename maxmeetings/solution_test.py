import unittest

from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solve(self):
        self.assertEqual([1, 2, 4, 5], solve([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
        self.assertEqual([6, 7, 1], solve(
            [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924],
            [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
        ))


if __name__ == '__main__':
    unittest.main()
