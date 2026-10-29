class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        for u in reversed(order):
            max_size = 0

            for v in adj[u]:
                if v != parent[u]:
                    size[u] += size[v]

                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        current = 0

        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = current
                current += 1

                for v in adj[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Build iterative segment tree
        seg = [0] * (2 * n)
        chars = list(s)

        for i in range(n):
            seg[n + pos[i]] = 1 << (ord(chars[i]) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(u, c):
            p = n + pos[u]
            seg[p] = 1 << (ord(c) - ord('a'))

            while p > 1:
                p //= 2
                seg[p] = seg[p * 2] ^ seg[p * 2 + 1]

        def range_query(l, r):
            l += n
            r += n + 1
            result = 0

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1

                if r & 1:
                    r -= 1
                    result ^= seg[r]

                l //= 2
                r //= 2

            return result

        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_query(pos[u], pos[v])
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(u, c)

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_query(u, v)

                # At most one character has odd frequency
                answer.append((mask & (mask - 1)) == 0)

        return answer
