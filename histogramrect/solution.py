def solve(histogram: list, size: int) -> int:
    max_rect = 0
    block_stack = []

    def calculate(anchor, prev_max, stack):
        current_i = stack.pop()
        calculated = histogram[current_i] * ((anchor - stack[-1] - 1) if stack else anchor)
        return max(calculated, prev_max)

    i = 0
    while i < size:
        if (not block_stack) or (histogram[i] >= histogram[block_stack[-1]]):
            block_stack.append(i)
            i += 1
        else:
            max_rect = calculate(i, max_rect, block_stack)

    while block_stack:
        max_rect = calculate(i, max_rect, block_stack)

    return max_rect
