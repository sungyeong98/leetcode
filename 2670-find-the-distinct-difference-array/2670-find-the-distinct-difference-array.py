class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            pref=len(set(nums[:i+1]))
            suff=len(set(nums[i+1:]))
            result.append(pref-suff)
        return result