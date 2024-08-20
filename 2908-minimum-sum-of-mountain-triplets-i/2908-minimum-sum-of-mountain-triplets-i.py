class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result=-1
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]>=nums[j]:
                    continue
                for k in range(j+1,n):
                    if nums[j]>nums[k]:
                        if result==-1:
                            result=nums[i]+nums[j]+nums[k]
                        else:
                            result=min(result, nums[i]+nums[j]+nums[k])
        return result