class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1,p2=0,0
        for idx,(val1,val2) in enumerate(zip(player1,player2)):
            if idx>0 and player1[idx-1]==10:
                p1+=val1*2
            elif idx>1 and player1[idx-2]==10:
                p1+=val1*2
            else:
                p1+=val1
            
            if idx>0 and player2[idx-1]==10:
                p2+=val2*2
            elif idx>1 and player2[idx-2]==10:
                p2+=val2*2
            else:
                p2+=val2
        if p1>p2:   return 1
        elif p2>p1: return 2
        return 0