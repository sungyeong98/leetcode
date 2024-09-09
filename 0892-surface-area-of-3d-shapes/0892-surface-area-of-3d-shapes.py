class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        result=0
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    result+=(grid[row][col]*4)+2
                if row:
                    result-=min(grid[row][col], grid[row-1][col])*2
                if col:
                    result-=min(grid[row][col], grid[row][col-1])*2
        return result