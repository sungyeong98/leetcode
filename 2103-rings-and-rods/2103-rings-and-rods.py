class Solution:
    def countPoints(self, rings: str) -> int:
        temp=[[-100,-100,-100] for _ in range(10)]

        for i in range(0,len(rings)-1,2):
            color=rings[i]
            pos=int(rings[i+1])
            idx=0

            if color=='R':      idx=0
            elif color=='G':    idx=1
            else:               idx=2

            temp[pos][idx]=1
        
        result=0
        for i in temp:
            if sum(i)==3:
                result+=1
        return result