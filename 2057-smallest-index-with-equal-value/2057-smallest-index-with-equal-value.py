class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        result=-1
        for idx,val in enumerate(nums):
            if idx%10==val:
                return idx
        return result