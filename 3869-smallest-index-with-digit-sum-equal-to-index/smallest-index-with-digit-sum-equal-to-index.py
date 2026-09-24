class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if self.sumOfDigits(nums[i]) == i:
                return i
        
        return -1

    def sumOfDigits(self, num):
        total = 0
        
        while num > 0:
            total += num % 10
            num //= 10
        
        return total