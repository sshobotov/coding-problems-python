class Solver:
    @staticmethod
    def find(arr: list) -> int:
        longest = len('{0:b}'.format(max(arr)))
        pattern = '{0:0' + str(longest) + 'b}'

        values = [[int(y) for y in pattern.format(x)] for x in arr]
        result = '0b'

        for i in range(longest):
            i_sum = 0
            for j in values:
                i_sum += j[i]

            result += str(i_sum % 3)

        return int(result, 2)

