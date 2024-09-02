class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        idx1={val:idx for idx,val in enumerate(s1)}
        idx2={val:idx for idx,val in enumerate(s2)}
        s=set(s1+s2)
        for i in s:
            if i not in idx1 or i not in idx2:
                return False
            
            if idx1[i]!=idx2[i] and abs(idx1[i]-idx2[i])!=2:
                return False
        return True