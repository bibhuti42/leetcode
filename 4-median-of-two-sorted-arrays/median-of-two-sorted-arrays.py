class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Correct partition
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(max(left1, left2))

                return (
                    max(left1, left2) + min(right1, right2)
                ) / 2.0

            # We took too many elements from nums1
            elif left1 > right2:
                right = i - 1

            # We took too few elements from nums1
            else:
                left = i + 1