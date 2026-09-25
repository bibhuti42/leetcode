class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)

        def parse(i):
            """
            Returns:
                (set of generated strings, next index)
            """
            result = set()
            current = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    # Union current expression into result
                    result.update(current)
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    # Parse content inside braces
                    inside, i = parse(i + 1)

                    # Concatenate current with inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                else:
                    # Normal lowercase character
                    ch = expression[i]

                    current = {
                        s + ch
                        for s in current
                    }

                    i += 1

            # Add the last expression
            result.update(current)

            # Skip '}'
            if i < n and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)