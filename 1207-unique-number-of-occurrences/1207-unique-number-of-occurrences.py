from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n=Counter(arr)
        if len(n)==len(set(n.values())):
            return True
        return False