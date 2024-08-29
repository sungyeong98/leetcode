class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        result=float('inf')
        for i in range(n-1,-2+k,-1):
            high=nums[i]
            for j in range(i-k+1,-1,-1):
                result=min(result,high-nums[j])
        return result