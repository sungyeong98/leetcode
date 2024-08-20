class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        result=[nums[i+1]-nums[i] for i in range(len(nums)-1)]
        return min(result)