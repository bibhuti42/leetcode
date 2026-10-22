class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        k = nums.index(0)

        # Circular increasing order
        if all((nums[i] + 1) % n == nums[(i + 1) % n]
               for i in range(n)):

            # Rotate left k times
            ans = min(ans, k)

            # Rotate right using two reversals
            ans = min(ans, n - k + 2)

        # Circular decreasing order
        if all((nums[i] - 1) % n == nums[(i + 1) % n]
               for i in range(n)):

            # Rotate left, then reverse
            ans = min(ans, (k + 1) % n + 1)

            # Reverse, then rotate left
            ans = min(ans, (n - 1 - k) % n + 1)

        return -1 if ans == float('inf') else ans
