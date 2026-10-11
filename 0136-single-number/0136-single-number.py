class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        numsdict = {}

        for num in nums:
            if num in numsdict:
                numsdict[num] +=1
                continue
            numsdict[num] = 1

        for key, value in numsdict.items():
            if value == 1:
                return key