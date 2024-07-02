class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result=0
        s=bin(start)[2:]
        g=bin(goal)[2:]
        if len(s)<len(g):   s='0'*(len(g)-len(s))+s
        elif len(s)>len(g): g='0'*(len(s)-len(g))+g
        for i,j in zip(s,g):
            if i!=j:
                result+=1
        return result