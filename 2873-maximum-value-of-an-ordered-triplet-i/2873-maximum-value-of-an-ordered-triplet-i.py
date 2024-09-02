class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]>nums[j]:
                    for k in range(j+1,n):
                        result=max(result,(nums[i]-nums[j])*nums[k])
        return result