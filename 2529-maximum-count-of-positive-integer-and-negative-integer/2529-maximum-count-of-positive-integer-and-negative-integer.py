class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=len([i for i in nums if i>0])
        neg=len([i for i in nums if i<0])
        if pos>neg: return pos
        return neg