from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=Counter(nums)
        return [i for i in n.keys() if n[i]==2]