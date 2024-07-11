from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return True if len(list(set(Counter(s).values())))==1 else False