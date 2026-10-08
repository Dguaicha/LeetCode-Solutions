class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        text=str(x)
        j = len(text)-1

        if text[0] == '-':
            return False
        if len(text)==1:
            return True
        for i in range(0, len(text)-1, 1):
            if text[i]!=text[j]:
                return False   
            j=j-1     
        return True
        


