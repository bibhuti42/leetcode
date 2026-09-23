class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        # If we need to remove the entire array
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            # Shrink window if sum exceeds target
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            # Found required subarray
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len