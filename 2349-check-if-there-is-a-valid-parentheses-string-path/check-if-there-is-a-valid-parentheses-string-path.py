class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        # dp[j] = set of possible balances at cell (i, j)
        dp = [set() for _ in range(n)]
        dp[0].add(1)  # grid[0][0] must be '('

        for j in range(1, n):
            if dp[j-1]:
                delta = 1 if grid[0][j] == '(' else -1
                dp[j] = {b + delta for b in dp[j-1] if b + delta >= 0}

        for i in range(1, m):
            delta = 1 if grid[i][0] == '(' else -1
            new_dp = [set() for _ in range(n)]
            new_dp[0] = {b + delta for b in dp[0] if b + delta >= 0}
            for j in range(1, n):
                delta = 1 if grid[i][j] == '(' else -1
                combined = dp[j] | new_dp[j-1]
                new_dp[j] = {b + delta for b in combined if b + delta >= 0}
            dp = new_dp

        return 0 in dp[n-1]