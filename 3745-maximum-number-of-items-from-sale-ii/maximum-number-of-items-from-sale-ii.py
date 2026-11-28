from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Count the frequency of each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Calculate maximum eligible free copies
        free = [0] * (n + 1)

        for factor in range(1, n + 1):
            if freq[factor] == 0:
                continue

            for multiple in range(factor, n + 1, factor):
                free[factor] += freq[multiple]

            # Exclude the purchased item itself
            free[factor] -= 1

        # Step 3: Find the cheapest item
        min_price = min(price for factor, price in items)

        # Step 4: Identify beneficial purchases
        offers = []

        for factor, price in items:
            if free[factor] > 0 and price < 2 * min_price:
                offers.append((price, free[factor]))

        # Step 5: Sort offers by purchase price
        offers.sort()

        # Step 6: Buy items that provide free copies
        ans = 0

        for price, count in offers:
            quantity = min(count, budget // price)

            ans += 2 * quantity
            budget -= quantity * price

        # Step 7: Spend remaining budget on the cheapest item
        ans += budget // min_price

        return ans