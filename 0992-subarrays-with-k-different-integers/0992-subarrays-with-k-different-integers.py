class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k)-self.helper(nums,k-1)
    
    def helper(self, nums, k):
        result=0
        count=[0]*(len(nums)+1)
        
        l=0
        for r in range(len(nums)):
            count[nums[r]]+=1
            if count[nums[r]]==1:
                k-=1
            while k==-1:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    k+=1
                l+=1
            result+=r-l+1
        return result