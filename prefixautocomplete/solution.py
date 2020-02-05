import unittest
from typing import List, Optional


class _TrieNode:
    def __init__(self, children={}, is_word=False):
        self.children = children
        self.is_word = is_word


def __append(root: _TrieNode, word: str):
    node = root

    for c in word:
        if c not in node.children:
            node.children[c] = _TrieNode()

        node = node.children[c]

    node.is_word = True


def __find(root: _TrieNode, prefix: str) -> Optional[_TrieNode]:
    node = root

    for c in prefix:
        if c not in node.children:
            return None

        node = node.children[c]

    return node


def __words(node: _TrieNode, word: str) -> List[str]:
    acc = [] if not node.is_word else word

    for c, n in node.children.items():
        acc += __words(n, word + c)

    return acc


def solve(given: List[str], query: str) -> List[str]:
    root = _TrieNode()
    for w in given:
        __append(root, w)

    found = __find(root, query)
    if found is None:
        return []
    else:
        return __words(found, query)


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertListEqual(["deer", "deal"], solve(["dog", "deer", "deal"], "de"))


if __name__ == '__main__':
    unittest.main()
