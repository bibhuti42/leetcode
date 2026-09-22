class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # existing code here

        n = len(nums)

        class Node:
            def __init__(self):
                self.prod = 1 % k
                self.pref = [0] * k

        def merge(left: Node, right: Node) -> Node:
            res = Node()

            # Product of whole segment
            res.prod = (left.prod * right.prod) % k

            # Prefixes from left part
            for i in range(k):
                res.pref[i] += left.pref[i]

            # Prefixes crossing into right part
            for i in range(k):
                if right.pref[i]:
                    res.pref[(left.prod * i) % k] += right.pref[i]

            return res

        # Build segment tree
        size = 1
        while size < n:
            size *= 2

        tree = [Node() for _ in range(2 * size)]

        def make_node(value):
            node = Node()
            rem = value % k
            node.prod = rem
            node.pref[rem] = 1
            return node

        for i in range(n):
            tree[size + i] = make_node(nums[i])

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        # Update one index
        def update(index, value):
            pos = size + index
            tree[pos] = make_node(value)

            pos //= 2
            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        # Query range [l, r]
        def query(l, r):
            left_nodes = []
            right_nodes = []

            l += size
            r += size

            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(tree[l])
                    l += 1

                if r % 2 == 0:
                    right_nodes.append(tree[r])
                    r -= 1

                l //= 2
                r //= 2

            ans = Node()

            # Merge left to right
            for node in left_nodes:
                ans = merge(ans, node)

            for node in reversed(right_nodes):
                ans = merge(ans, node)

            return ans

        result = []

        for index, value, start, x in queries:
            update(index, value)

            # Remaining array after removing prefix nums[0:start]
            node = query(start, n - 1)

            result.append(node.pref[x])

        return result