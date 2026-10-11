class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        Max = 0

        for phrase in sentences:
            words = phrase.split()
            if len(words) > Max:
                Max = len(words)
        
        return Max