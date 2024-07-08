class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result=[0]*len(s)
        dir={'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}

        for i in range(len(s)):
            x, y = startPos[0], startPos[1]
            ins=s[i:]
            cnt=0

            for char in ins:
                dx, dy = dir[char]
                if 0<=x+dx<n and 0<=y+dy<n:
                    cnt+=1
                    x,y=x+dx,y+dy
                else:
                    break
            
            result[i]=cnt
        return result