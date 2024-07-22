class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n=len(grid),len(grid[0])
        balls=[(0,i) for i in range(n)]
        result=[]

        for (x,y) in balls:
            while x<=m-1:
                dir=grid[x][y]
                if dir==1 and y+1<n and grid[x][y+1]!=-1:
                    x+=1
                    y+=1
                elif dir==-1 and y-1>=0 and grid[x][y-1]!=1:
                    x+=1
                    y-=1
                else:
                    break
            if x==m:
                result.append(y)
            else:
                result.append(-1)
        return result