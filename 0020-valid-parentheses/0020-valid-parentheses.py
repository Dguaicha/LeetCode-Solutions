class Solution:
    def isValid(self, s):
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        # Stack to keep track of opening brackets
        stack = []

        # Loop through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty; otherwise use a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False  # Mismatch found
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack