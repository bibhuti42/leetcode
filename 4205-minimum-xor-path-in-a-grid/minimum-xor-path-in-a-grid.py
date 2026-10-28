class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                prev = 0

                if i == 0 and j == 0:
                    prev = 1
                else:
                    if i > 0:
                        prev |= dp[i - 1][j]
                    if j > 0:
                        prev |= dp[i][j - 1]

                mask = 0

                while prev:
                    bit = prev & -prev
                    xor_val = bit.bit_length() - 1
                    mask |= 1 << (xor_val ^ val)
                    prev ^= bit

                dp[i][j] = mask

        result = dp[m - 1][n - 1]

        return (result & -result).bit_length() - 1