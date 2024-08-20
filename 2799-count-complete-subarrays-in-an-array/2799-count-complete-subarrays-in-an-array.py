class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target=set(nums)
        n=len(nums)
        result=0
        for i in range(n-len(target)+1):
            for j in range(i+1,n+1):
                if set(nums[i:j])==target:
                    result+=(n-j+1)
                    break
        return result