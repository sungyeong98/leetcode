class Solution:
    def numSplits(self, s: str) -> int:
        result=0
        for i in range(1,len(s)):
            if len(set(s[:i]))==len(set(s[i:])):
                result+=1
        return result