def solve(n: int, steps: set) -> int:
    return __solve_rec(steps, n, {})


def __solve_rec(steps: set, left: int, memo: map) -> int:
    if left == 0:
        return 1
    if left < 0:
        return 0
    if left in memo:
        return memo[left]

    result = 0
    for n in steps:
        result += __solve_rec(steps, left - n, memo)

    memo[left] = result
    return result
