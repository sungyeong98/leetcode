class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp=sorted(nums)
        if temp[-1]>=temp[-2]*2:
            return nums.index(temp[-1])
        return -1