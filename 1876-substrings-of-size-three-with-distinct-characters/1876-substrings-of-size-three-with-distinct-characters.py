class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result=0
        while len(s)>=3:
            temp=s[-3:]
            if len(set(temp))==3:
                result+=1
            s=s[:-1]
        return result