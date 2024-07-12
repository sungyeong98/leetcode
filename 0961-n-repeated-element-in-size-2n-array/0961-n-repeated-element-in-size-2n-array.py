from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=Counter(nums)
        return [i for i in n.keys() if n[i]==max(n.values())][0]