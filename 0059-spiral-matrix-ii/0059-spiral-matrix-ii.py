class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result=[[0]*n for _ in range(n)]

        num=1
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        state=0
        x,y=0,0
        while num<=n**2:
            while 0<=x<n and 0<=y<n and result[x][y]==0:
                result[x][y]=num
                num+=1
                x, y = x+dir[state][0], y+dir[state][1]

            x, y = x - dir[state][0], y - dir[state][1]

            state = (state + 1) % 4
            x, y = x + dir[state][0], y + dir[state][1]
        
        return result