class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return reduce(lambda x,y:set(x)&set(y),nums)