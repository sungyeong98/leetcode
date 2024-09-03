class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        for i in list(zip(*grid)):
            if len(set(i))!=1:
                return False
        for i in grid:
            for j in range(n-1):
                if i[j]==i[j+1]:
                    return False
        return True