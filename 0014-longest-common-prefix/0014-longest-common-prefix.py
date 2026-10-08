from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            strs2=[]
            index=0
            while True:
                try:
                    chars = [word[index] for word in strs]
                    if all(char == chars[0] for char in chars):
                        strs2.append(chars[0])
                        index += 1
                    else:
                        break
                except IndexError:
                    break
            combined="".join(strs2)
            return combined

"""AI GENERATED SOLUTION;
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
"""