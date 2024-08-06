class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=0,sum(nums)
        result=[]
        for i in range(n):
            right-=nums[i]
            temp=(nums[i]*i-left)+(right-nums[i]*(n-i-1))
            result.append(temp)
            left+=nums[i]
        return result