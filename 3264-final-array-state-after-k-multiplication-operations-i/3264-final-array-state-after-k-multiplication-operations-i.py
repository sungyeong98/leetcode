class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
            idx=nums.index(min(nums))
            nums[idx]*=multiplier
            k-=1
        return nums