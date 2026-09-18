class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first, last = {}, {}
        for i, ch in enumerate(s):
            first.setdefault(ch, i)
            last[ch] = i

        intervals = []
        for c in first:
            l, r = first[c], last[c]
            i, ok = l, True
            while i <= r:
                if first[s[i]] < l:      # would need to extend left -> invalid
                    ok = False
                    break
                r = max(r, last[s[i]])   # extend right to cover all occurrences
                i += 1
            if ok:
                intervals.append((r, l))

        intervals.sort()                 # by right endpoint
        res, prev_end = [], -1
        for r, l in intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r
        return res