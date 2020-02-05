import unittest


class TrieNode:
    def __init__(self, children={}, value=False):
        self.children = children
        self.value = value


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.value = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]

        return node.value

    def starts_with(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]

        return True


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        target = Trie()

        target.insert("apple")
        self.assertEqual(True, target.search("apple"))
        self.assertEqual(False, target.search("app"))
        self.assertEqual(True, target.starts_with("app"))

        target.insert("app")
        self.assertEqual(True, target.search("app"))


if __name__ == '__main__':
    unittest.main()
