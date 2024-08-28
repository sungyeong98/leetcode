class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        p={i:[0]*11 for i in range(n)}
        for i,j in pick:
            p[i][j]+=1
        result=0
        for i in p:
            if max(p[i])>i:
                result+=1
        return result