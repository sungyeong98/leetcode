class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        prev=sum(nums[:k])
        result=prev/k
        for i in range(1,n-k+1):
            prev-=nums[i-1]
            prev+=nums[i+k-1]
            result=max(result,prev/k)
        return result