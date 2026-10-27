
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)
        sign = 1
        result = 0

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits manually
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Step 4: Check overflow before updating
            limit = INT_MAX if sign == 1 else -INT_MIN

            if result > (limit - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
