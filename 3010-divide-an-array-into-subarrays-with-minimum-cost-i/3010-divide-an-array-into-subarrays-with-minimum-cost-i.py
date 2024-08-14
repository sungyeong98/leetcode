class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        result=float('inf')
        n=len(nums)
        for i in range(1,n-1):
            result=min(result, nums[0]+nums[i]+min(nums[i+1:]))
        return result