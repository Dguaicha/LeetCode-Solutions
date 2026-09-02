class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = set()
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if curr + nums[j] == target:
                    output.add(i)
                    output.add(j)
        return list(output)
        