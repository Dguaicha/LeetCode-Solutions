class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_hash_table = {}
        
        start = 0

        max_length = 0


        for end, char in enumerate(s):

            if char in char_hash_table and char_hash_table[char] >= start:

                start = char_hash_table[char] + 1

            char_hash_table[char] = end

            max_length = max(max_length, end - start + 1)

        return max_length
