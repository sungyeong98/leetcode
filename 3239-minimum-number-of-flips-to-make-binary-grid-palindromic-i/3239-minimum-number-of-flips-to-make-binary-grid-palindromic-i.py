class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n=len(grid)//2, len(grid[0])//2
        row,col=0,0

        row=sum(row[i]^row[~i] for i in range(n) for row in grid)
        grid=zip(*grid)
        
        for r in grid:
            for i in range(m):
                col+=r[i]^r[~i]
        return min(row,col)