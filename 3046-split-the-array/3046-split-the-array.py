class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c=Counter(nums)
        if max(c.values())>2:
            return False
        return True