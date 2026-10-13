
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square all elements
        nums = sorted(x * x for x in nums)

        n = len(nums)
        negative_count = n // 2

        # Subtract smaller squares, add larger squares
        return sum(nums[negative_count:]) - sum(nums[:negative_count])
