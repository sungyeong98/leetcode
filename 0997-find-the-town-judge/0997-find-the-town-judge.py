class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p={i:0 for i in range(1,n+1)}
        for a,_ in trust:
            p[a]+=1
        result=[i for i in p.keys() if p[i]==0]
        return result[0] if result else -1