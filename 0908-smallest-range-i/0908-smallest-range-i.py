class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num,min_num=max(nums),min(nums)
        if max_num-min_num<=k*2:
            return 0
        return max_num-min_num-k*2