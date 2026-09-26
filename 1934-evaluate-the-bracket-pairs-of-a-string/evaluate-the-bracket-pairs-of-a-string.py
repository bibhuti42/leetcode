class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kv = {k: v for k, v in knowledge}
        out, key, inside = [], [], False

        for c in s:
            if c == '(':
                inside, key = True, []
            elif c == ')':
                inside = False
                out.append(kv.get(''.join(key), '?'))
            elif inside:
                key.append(c)
            else:
                out.append(c)

        return ''.join(out)