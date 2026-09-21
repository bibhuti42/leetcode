class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            num %= k

            # curr[r] = number of subarrays ending at current position
            # whose product % k == r
            curr = [0] * k

            # Subarray containing only nums[i]
            curr[num] += 1

            # Extend all previous subarrays with nums[i]
            for remainder in range(k):
                new_remainder = (remainder * num) % k
                curr[new_remainder] += dp[remainder]

            # Every subarray ending here contributes to final answer
            for remainder in range(k):
                result[remainder] += curr[remainder]

            dp = curr

        return result