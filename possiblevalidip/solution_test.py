import unittest
from .solution import find


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual(["0.0.0.0"], find("0000", 4))
        self.assertListEqual([], find("00000", 6))
        self.assertListEqual(["255.255.11.135", "255.255.111.35"], find("25525511135", 11))
        self.assertListEqual(["111.110.11.111", "111.110.111.11"], find("11111011111", 11))


if __name__ == '__main__':
    unittest.main()
