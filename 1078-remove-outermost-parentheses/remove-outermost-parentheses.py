class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for ch in s:
            if ch == '(':
                # If depth > 0, this is not an outermost '('
                if depth > 0:
                    result.append(ch)
                depth += 1

            else:  # ch == ')'
                depth -= 1

                # If depth > 0 after decrementing,
                # this is not an outermost ')'
                if depth > 0:
                    result.append(ch)

        return ''.join(result)