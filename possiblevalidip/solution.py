def find(digits: str, size: int) -> list:
    if size < 4 or size > 12:
        return []

    return __find_rec(digits, size, 0, [])


def __find_rec(digits: str, size: int, pos: int, address: list) -> list:
    if pos == size:
        return [".".join(address)] if len(address) == 4 else []
    elif len(address) == 4:
        return []

    res1 = __find_rec(digits, size, pos + 1, address + [digits[pos:pos + 1]])
    res2 = __find_rec(digits, size, pos + 2, address + [digits[pos:pos + 2]]) \
        if digits[pos] != "0" and pos + 2 <= size else []
    res3 = __find_rec(digits, size, pos + 3, address + [digits[pos:pos + 3]]) \
        if digits[pos] != "0" and pos + 3 <= size and int(digits[pos:pos + 3]) < 256 else []
    return res1 + res2 + res3
