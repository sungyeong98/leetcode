class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt=0
        if set(s1)!=set(s2):
            return False
        c1,c2=Counter(s1),Counter(s2)
        for i in set(s1+s2):
            if i not in c1 or i not in c2:
                return False
            if c1[i]!=c2[i]:
                return False

        for i,j in zip(s1,s2):
            if i!=j:
                cnt+=1
        if cnt>2:
            return False
        return True