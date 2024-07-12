from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=Counter(nums)
        return n.most_common(1)[0][0]