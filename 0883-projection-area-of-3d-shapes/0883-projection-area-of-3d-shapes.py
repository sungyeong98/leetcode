class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        result=n*n
        for i in grid:
            result+=max(i)
            result-=i.count(0)
        for i in list(zip(*grid)):
            result+=max(list(i))
        return result