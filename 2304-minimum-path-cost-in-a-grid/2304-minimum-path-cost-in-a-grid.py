class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        dp=[grid[0][j] for j in range(n)]

        for i in range(1,m):
            temp=[float('inf')]*n
            for j in range(n):
                for k in range(n):
                    temp[k]=min(temp[k],dp[j]+moveCost[grid[i-1][j]][k]+grid[i][k])
            dp=temp

        return min(dp)