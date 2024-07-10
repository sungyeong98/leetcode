from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n=Counter(nums)
        max_num=max(n.values())
        return len([i for i in n.keys() if n[i]==max_num])*max_num