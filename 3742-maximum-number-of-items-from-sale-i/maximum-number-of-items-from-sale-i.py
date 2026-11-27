from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(factor for factor, price in items)

        # Count the frequency of each factor
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Calculate free copies for each factor
        free = [0] * (max_factor + 1)

        for factor in range(1, max_factor + 1):
            if freq[factor] == 0:
                continue

            for multiple in range(factor, max_factor + 1, factor):
                free[factor] += freq[multiple]

            free[factor] -= 1

        # Find the cheapest item
        min_price = min(price for factor, price in items)

        # 0/1 Knapsack for first-time purchases
        dp = [0] * (budget + 1)

        for factor, price in items:
            value = 1 + free[factor]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        # Spend remaining budget on the cheapest item
        ans = 0

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // min_price)

        return ans