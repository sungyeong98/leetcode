class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        temp=[]

        for i in range(m):
            temp.append((i,0))
        for j in range(n):
            temp.append((0,j))
        temp.pop(0)

        result=[[0]*n for _ in range(m)]

        for i,j in temp:
            val=[]
            x,y=i,j
            while 0<=x<m and 0<=y<n:
                val.append(grid[x][y])
                x+=1
                y+=1
            idx=0
            while idx<len(val):
                print(val,val[:idx],val[idx+1:],idx)
                result[i+idx][j+idx]=abs(len(set(val[:idx]))-len(set(val[idx+1:])))
                idx+=1
        return result