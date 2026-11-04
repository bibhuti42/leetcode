
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        size = len(values)
        rank = {v: i + 1 for i, v in enumerate(values)}

        bit_count = [0] * (size + 1)
        bit_sum = [0] * (size + 1)

        def update(value, delta):
            i = rank[value]
            while i <= size:
                bit_count[i] += delta
                bit_sum[i] += delta * value
                i += i & -i

        def prefix(i):
            count = total = 0
            while i > 0:
                count += bit_count[i]
                total += bit_sum[i]
                i -= i & -i
            return count, total

        def kth(kth_pos):
            i = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = i + step
                if nxt <= size and bit_count[nxt] < kth_pos:
                    kth_pos -= bit_count[nxt]
                    i = nxt
                step >>= 1

            return i + 1

        # Step 1: Calculate cost for each window
        for i in range(x):
            update(nums[i], 1)

        window_sum = sum(nums[:x])
        costs = []

        for start in range(n - x + 1):
            median_idx = kth((x + 1) // 2)
            median = values[median_idx - 1]

            left_count, left_sum = prefix(median_idx)

            cost = (
                median * left_count - left_sum
                + (window_sum - left_sum)
                - median * (x - left_count)
            )

            costs.append(cost)

            if start + x < n:
                update(nums[start], -1)
                update(nums[start + x], 1)

                window_sum += nums[start + x] - nums[start]

        # Step 2: DP to select k non-overlapping windows
        INF = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                # Skip current position
                skip = curr[i - 1]

                # Select window ending at i - 1
                take = prev[i - x] + costs[i - x]

                curr[i] = min(skip, take)

            prev = curr

        return prev[n]
