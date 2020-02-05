import unittest

from .solution import sort


class SolutionTestCase(unittest.TestCase):
    def test_sort(self):
        self.assertEqual([1, 1, 2, 2, 4, 5, 7], sort([1, 4, 1, 2, 7, 5, 2]))


if __name__ == '__main__':
    unittest.main()
