class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            # Opening bracket
            if char in "([{":
                stack.append(char)

            # Closing bracket
            else:
                # No opening bracket available
                if not stack:
                    return False

                # Check whether latest opening bracket matches
                if stack.pop() != brackets[char]:
                    return False

        # Stack should be empty if all brackets matched
        return len(stack) == 0