
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 30

        # Count set bits at every bit position
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    bit_count[bit] += 1

        result = 0

        # Construct k maximum possible numbers
        for _ in range(k):
            current = 0

            for bit in range(30):
                if bit_count[bit] > 0:
                    current |= (1 << bit)
                    bit_count[bit] -= 1

            result = (result + current * current) % MOD

        return result
