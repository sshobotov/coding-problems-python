from typing import Optional


def solve(n: int) -> Optional[list]:
    if n <= 0:
        return None

    return __solve_rec(n, 0, 0, [], set(), set(), set())


def __solve_rec(n: int, col: int, row: int, res: list, taken_row: set, taken_diagonal: set, taken_r_diagonal: set):
    if len(res) == n:
        return res
    if col == n or row == n:
        return None

    step_result = None
    if row not in taken_row and \
       (row + col) not in taken_diagonal and \
       (row - col + n - 1) not in taken_r_diagonal:
        step_result = __solve_rec(n, col + 1, 0, res + [(col, row)], taken_row.union({row}),
                                  taken_diagonal.union({row + col}), taken_r_diagonal.union({row - col + n - 1}))

    if step_result is None:
        return __solve_rec(n, col, row + 1, res, taken_row, taken_diagonal, taken_r_diagonal)
    else:
        return step_result
