class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                min_open -= 1
                max_open -= 1

            else:  # '*'
                # '*' can act as ')' for minimum
                # or '(' for maximum
                min_open -= 1
                max_open += 1

            # Too many ')' even when all '*' are treated as '('
            if max_open < 0:
                return False

            # Number of unmatched '(' cannot be negative
            min_open = max(min_open, 0)

        return min_open == 0