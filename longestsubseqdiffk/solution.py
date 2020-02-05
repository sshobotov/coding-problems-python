def find(string: str, k: int, alphabet: int = 26, first_letter: str = 'a') -> int:
    size = len(string)
    dp = [0] * size
    max_length = [0] * alphabet

    first_i = ord(first_letter)

    for i in range(size):
        c_i = ord(string[i]) - first_i
        for j in range(max(c_i - k, 0), min(c_i + k, alphabet - 1) + 1):
            dp[i] = max(dp[i], max_length[j] + 1)
        max_length[c_i] = max(dp[i], max_length[c_i])

    return max(dp)
