class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                # Start a new inner score
                stack.append(0)

            else:
                # Score inside the current pair
                inner = stack.pop()

                # () -> 1
                # (A) -> 2 * A
                score = max(2 * inner, 1)

                # Add to the outer level
                stack[-1] += score

        return stack[0]