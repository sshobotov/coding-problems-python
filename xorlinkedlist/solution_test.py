import unittest
from .solution import XorLinkedList


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        target = XorLinkedList()
        self.assertIsNone(target.get(1))

        target.add(5)
        self.assertIsNone(target.get(1))

        target.add(10)
        self.assertEqual(10, target.get(1))

        target.add(15)
        self.assertEqual(10, target.get(1))


if __name__ == '__main__':
    unittest.main()
