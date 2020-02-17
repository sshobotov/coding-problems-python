class Solver:
    @staticmethod
    def find(arr: list, needle) -> bool:
        stack = sorted(arr)
        while True:
            stack_len = len(stack)
            if stack_len == 0:
                return False
            if stack_len == 1:
                return stack[0] == needle

            mid_index = stack_len // 2
            if stack[mid_index] == needle:
                return True
            if stack[mid_index] > needle:
                stack = stack[:mid_index]
            else:
                stack = stack[mid_index + 1:]
