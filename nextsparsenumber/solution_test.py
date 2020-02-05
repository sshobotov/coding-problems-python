import unittest

from .solution import find


class SolutionTestCase(unittest.TestCase):
    def test_find(self):
        self.assertEqual(4, find(4))
        self.assertEqual(8, find(6))
        self.assertEqual(40, find(38))
        self.assertEqual(64, find(44))


if __name__ == '__main__':
    unittest.main()
