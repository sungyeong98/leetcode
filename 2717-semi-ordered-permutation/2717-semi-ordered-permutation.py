class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        left=nums.index(1)
        right=nums.index(n)
        result=left-right+n-1-(left>right)
        return result