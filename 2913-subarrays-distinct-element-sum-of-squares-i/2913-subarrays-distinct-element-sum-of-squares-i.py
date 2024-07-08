class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                result+=(len(list(set(nums[i:j]))))**2
        return result