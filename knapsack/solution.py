def solve(val: list, wt: list, cap: int) -> int:
    memo = [[(val[i], wt[i])] if wt[i] <= cap else [(0, 0)] for i in range(len(val))]
    v_max = max(val)
    for i in range(1, len(memo)):
        for j in memo[i - 1]:
            (j_v, j_w) = j
            i_w = wt[i] + j_w
            if i_w <= cap:
                i_v = val[i] + j_v
                memo[i].append((i_v, i_w))
                if i_v > v_max:
                    v_max = i_v

            memo[i].append(j)

    return v_max


def __solve_rec(val: list, wt: list, n: int, cap: int) -> int:
    if cap == 0 or n == 0:
        return 0

    if wt[n - 1] > cap:
        return __solve_rec(val, wt, n - 1, cap)

    return max(
        val[n - 1] + __solve_rec(val, wt, n - 1, cap - wt[n - 1]),
        __solve_rec(val, wt, n - 1, cap)
    )
