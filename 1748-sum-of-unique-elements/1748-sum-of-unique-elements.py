from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([i for i in Counter(nums).keys() if Counter(nums)[i]==1])