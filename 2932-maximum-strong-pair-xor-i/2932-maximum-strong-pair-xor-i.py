class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result,n=0,len(nums)
        for i in range(n):
            for j in range(n):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    temp=nums[i]^nums[j]
                    if temp>result:
                        result=temp
        return result