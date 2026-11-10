class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        a, b, c = float('inf'), float('inf'), 0

        for cost in costs:
            current = cost + min(c + 1, b + 4, a + 9)
            a, b, c = b, c, current

        return c