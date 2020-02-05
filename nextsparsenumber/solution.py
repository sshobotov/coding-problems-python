def find(num: int) -> int:
    target = bin(num)[:1:-1]
    size = len(target)
    pos = 0

    while pos < size:
        if target[pos] == '1':
            if pos + 1 == size:
                break

            if target[pos + 1] == '1':
                first_zero = target.find('0', pos + 2)

                if first_zero == -1:
                    target = '0' * size + '1'
                    break

                target = '0' * first_zero + '1' + target[first_zero + 1:]
                pos = first_zero - 1

        pos += 1

    return int('0b' + target[::-1], 2)
