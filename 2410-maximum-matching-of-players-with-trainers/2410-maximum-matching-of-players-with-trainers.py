class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p=sorted(players)
        t=sorted(trainers)
        result=0
        i,j=0,0
        while i<len(p) and j<len(t):
            if p[i]<=t[j]:
                result+=1
                i+=1
                j+=1
            else:
                j+=1
        return result