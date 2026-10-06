class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        moves = 0

        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    # Match this ')' with an existing '('
                    open_count -= 1
                else:
                    # No '(' available, so we need to insert one
                    moves += 1

        # Any remaining '(' need corresponding ')'
        return moves + open_count