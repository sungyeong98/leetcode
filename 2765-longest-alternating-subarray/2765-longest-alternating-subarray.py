class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        result,dp=-1,-1
        for i in range(1,n):
            if dp>0 and nums[i]==nums[i-2]:
                dp+=1
            else:
                dp=2 if nums[i]==nums[i-1]+1 else -1
            result=max(result,dp)
        return result