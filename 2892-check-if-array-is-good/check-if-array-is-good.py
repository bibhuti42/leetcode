class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        cnt = Counter(nums)
        if cnt[n] != 2:
            return False
        return all(cnt[i] == 1 for i in range(1, n))