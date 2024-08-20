class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n=len(nums)
        temp=[]
        for i in range(n-1):
            temp.append(nums[i]+nums[i+1])
        
        return True if len(temp)!=len(set(temp)) else False