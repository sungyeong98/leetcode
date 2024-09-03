class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        for i in grid:
            if len(set(i))!=n:
                return False
        for i in list(zip(*grid)):
            if len(set(i))!=1:
                return False
        return True