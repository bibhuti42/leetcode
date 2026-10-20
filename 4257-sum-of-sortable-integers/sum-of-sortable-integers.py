class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        def can_rotate_to_sorted(arr):
            drops = 0
            m = len(arr)

            for i in range(m):
                if arr[i] > arr[(i + 1) % m]:
                    drops += 1

                if drops > 1:
                    return False

            return True

        def is_sortable(k):
            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]

                if Counter(block) != Counter(target):
                    return False

                if not can_rotate_to_sorted(block):
                    return False

            return True

        answer = 0

        for k in range(1, n + 1):
            if n % k == 0 and is_sortable(k):
                answer += k

        return answer