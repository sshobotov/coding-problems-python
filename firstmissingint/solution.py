from typing import Optional, List


def find(nums: List[int], size: int) -> Optional[int]:
    if size == 0:
        return None

    i = 0
    while i < size:
        current = nums[i]
        if current != i + 1:
            if 0 < current <= size:
                nums[i] = nums[current - 1]
                nums[current - 1] = current
            else:
                nums[i] = 0
                i += 1
        else:
            i += 1

    for i in range(size):
        if nums[i] == 0:
            return i + 1

    return None
