class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result,n=0,len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])<=nums[i]:
                    temp=nums[i]^nums[j]
                    if temp>result:
                        result=temp
        return result