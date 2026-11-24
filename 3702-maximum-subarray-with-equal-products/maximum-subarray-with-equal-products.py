
from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            product = 1
            current_gcd = 0
            current_lcm = 1

            for j in range(i, n):
                product *= nums[j]
                current_gcd = gcd(current_gcd, nums[j])
                current_lcm = lcm(current_lcm, nums[j])

                if product == current_gcd * current_lcm:
                    max_len = max(max_len, j - i + 1)

        return max_len
