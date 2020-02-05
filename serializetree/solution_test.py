import unittest
from .solution import Node, serialize_plain, deserialize_plain


class SolutionTestCase(unittest.TestCase):
    def test_both_ways(self):
        node = Node('')
        self.assertEqual('', deserialize_plain(serialize_plain(node)).val)

        node = Node('",')
        self.assertEqual('",', deserialize_plain(serialize_plain(node)).val)

        node = Node('root', None, Node("right", None, Node("right.right")))
        self.assertEqual('right.right', deserialize_plain(serialize_plain(node)).right.right.val)

        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual('left.left', deserialize_plain(serialize_plain(node)).left.left.val)


if __name__ == '__main__':
    unittest.main()
