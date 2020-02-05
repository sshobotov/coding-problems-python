def sort(values: list) -> list:
    min_value, max_value = min(values), max(values)
    counts = [0 for _ in range(min_value, max_value + 1)]

    # collect number of occurrences per value
    for i in values:
        rel_i = i - min_value
        counts[rel_i] = counts[rel_i] + 1

    # calculate max position per value
    for i in range(len(counts)):
        if i > 0:
            counts[i] += counts[i - 1]

    # assign each value its position and decrease position per duplicate
    result = [0 for _ in values]
    for i in values:
        rel_i = i - min_value

        result[counts[rel_i] - 1] = i
        counts[rel_i] -= 1

    return result
