class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:
        
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        total_diff = sum(diffs)

        # If we have enough operations to make every difference 0
        if k >= total_diff:
            return 0

        diffs.sort(reverse=True)
        diffs.append(0)  # sentinel

        n = len(diffs) - 1

        for i in range(n):
            current = diffs[i]
            next_val = diffs[i + 1]

            count = i + 1
            cost = (current - next_val) * count

            if k >= cost:
                # Reduce the first `count` values down to next_val
                k -= cost

            else:
                # We cannot completely reach next_val.
                # Distribute remaining operations as evenly as possible.
                reduce_each = k // count
                remainder = k % count

                new_val = current - reduce_each

                # First `remainder` values get reduced one additional time
                result = 0

                result += remainder * (new_val - 1) ** 2
                result += (count - remainder) * new_val ** 2

                # Remaining untouched differences
                for j in range(i + 1, n):
                    result += diffs[j] ** 2

                return result

        return 0