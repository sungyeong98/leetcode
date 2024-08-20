class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n-2):
            left=sum(nums[i:i+2])
            for j in range(i+1,n-1):
                right=sum(nums[j:j+2])
                if left==right:
                    return True
        return False