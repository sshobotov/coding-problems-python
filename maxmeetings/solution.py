def solve(s: list, f: list) -> list:
    sorted_by_finish = sorted(
        list(zip(range(len(f)), s, f)),
        key=lambda e: e[2]
    )

    result = [sorted_by_finish[0][0]]
    last_f = sorted_by_finish[0][2]

    for i in range(1, len(sorted_by_finish)):
        (c_i, c_s, c_f) = sorted_by_finish[i]

        if last_f <= c_s:
            last_f = c_f
            result.append(c_i)

    return list([x + 1 for x in result])
