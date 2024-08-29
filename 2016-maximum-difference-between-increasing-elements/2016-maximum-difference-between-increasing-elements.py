class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        result=-1
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    result=max(result,nums[j]-nums[i])
        return result