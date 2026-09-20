class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for position, char in enumerate(s, start=1):
            reverse_value = ord('z') - ord(char) + 1
            total += position * reverse_value

        return total