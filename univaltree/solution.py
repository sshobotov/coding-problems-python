import unittest


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solve(tree: Node) -> int:
    def __solve_rec(subtree: Node) -> int:
        value_l, cnt_l = (None, 0) if subtree.left is None else (subtree.left.value, __solve_rec(subtree.left))
        value_r, cnt_r = (None, 0) if subtree.right is None else (subtree.right.value, __solve_rec(subtree.right))

        return cnt_l + cnt_r + int(value_l == value_r)

    return __solve_rec(tree)


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1, solve(Node(1)))
        self.assertEqual(5, solve(Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))))


if __name__ == '__main__':
    unittest.main()
