from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def build(current: str, open_used: int, close_used: int):
            # If we've used all parentheses, it's a valid complete string
            if open_used == n and close_used == n:
                results.append(current)
                return

            # Add "(" if we still can
            if open_used < n:
                build(current + "(", open_used + 1, close_used)

            # Add ")" only if it wouldn't make it invalid
            if close_used < open_used:
                build(current + ")", open_used, close_used + 1)

        # Start building from empty string
        build("", 0, 0)

        results.sort()
        return results
