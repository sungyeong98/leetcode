class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left,right=0,sum(nums)
        n=len(nums)

        for i in range(n):
            if i==0:
                right-=nums[i]
            else:
                right-=nums[i]
                left+=nums[i-1]
            
            if left==right:
                return i
        return -1