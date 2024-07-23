class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        result,n=0,len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]==nums[j]:
                    continue
                for k in range(j+1,n):
                    if nums[i]!=nums[k] and nums[j]!=nums[k]:
                        result+=1
        return result