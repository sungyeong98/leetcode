class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        dp=[[[0]*(col+2) for _ in range(col+2)] for _ in range(row+1)]

        def count(r,c1,c2):
            result=0
            for nc1 in (c1-1,c1,c1+1):
                for nc2 in (c2-1,c2,c2+1):
                    result=max(result, dp[r+1][nc1+1][nc2+1])
            return result
        
        for r in reversed(range(row)):
            for c1 in range(min(col,r+2)):
                for c2 in range(max(0,col-r-1),col):
                    reward=grid[r][c1]+grid[r][c2]
                    if c1==c2:
                        reward/=2
                    dp[r][c1+1][c2+1]=reward+count(r,c1,c2)
        return dp[0][1][col]