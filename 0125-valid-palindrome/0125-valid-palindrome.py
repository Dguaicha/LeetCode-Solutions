import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s1)
        return s2 == s2[::-1]