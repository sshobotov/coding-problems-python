def solve(n: int) -> int:
    # n = 1
    # (1, A, C)
    #
    # n = 2
    # (1, A, B)
    # (2, A, C)
    # (1, B, C)
    #
    # n = 3
    # (1, A, C)
    # (2, A, B)
    # (1, C, B)
    # (3, A, C)
    # (1, B, A)
    # (2, B, C)
    # (1, A, C)
    #
    # n = 4
    # (1, A, B)
    # (2, A, C)
    # (1, B, C)
    # (3, A, B)
    # (1, C, A)
    # (2, C, B)
    # (1, A, B)
    # (4, A, C)
    # (1, B, C)
    # (2, B, A)
    # (1, C, A)
    # (3, B, C)
    # (1, A, B)
    # (2, A, C)
    # (1, B, C)
    return __solve_rec(n, "A", "C", "B")


def __solve_rec(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return 0

    acc = __solve_rec(n - 1, from_rod, aux_rod, to_rod)

    print("(" + ", ".join([str(n), from_rod, to_rod]) + ")")
    acc += 1

    acc += __solve_rec(n - 1, aux_rod, to_rod, from_rod)

    return acc
