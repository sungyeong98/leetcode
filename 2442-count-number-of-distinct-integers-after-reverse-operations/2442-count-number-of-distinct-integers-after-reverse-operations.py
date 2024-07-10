class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n=nums+[int(str(i)[::-1]) for i in nums]
        return len(list(set(n)))