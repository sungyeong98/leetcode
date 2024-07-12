class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        result=[0]*n
        for i in range(n):
            level=0
            while level<=m-1:
                if grid[level][i]>=0:
                    level+=1
                else:
                    result[i]+=(m-level)
                    break
        return sum(result)