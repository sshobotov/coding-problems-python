import unittest


def solve(encoded: str, alphabet_size=26) -> int:
    def __solve_rec(size, pos, memo) -> int:
        if pos == size:
            return 1
        if pos in memo:
            return memo[pos]
        if int(encoded[pos]) < 1:
            raise ValueError(f"Invalid input {encoded[pos]} at {pos}")

        cnt_1 = __solve_rec(size, pos + 1, memo)
        cnt_2 = 0
        if pos + 2 <= size and int(encoded[pos:pos+2]) <= alphabet_size:
            cnt_2 = __solve_rec(size, pos + 2, memo)

        cnt = cnt_1 + cnt_2
        memo[pos] = cnt_1

        return cnt

    try:
        return __solve_rec(len(encoded), 0, {})
    except ValueError:
        return 0


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1, solve(""))
        self.assertEqual(3, solve("111"))
        self.assertEqual(0, solve("001"))
        self.assertEqual(2, solve("1271"))


if __name__ == '__main__':
    unittest.main()
