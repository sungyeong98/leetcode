class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        result=[i for i in c.keys() if c[i]==1]
        return result[-1]