class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        result=0

        m,n=len(grid),len(grid[0])
        minx,miny,maxx,maxy=0,0,0,0

        for idx,val in enumerate(list(zip(*grid))):
            if 1 in list(val):
                miny=idx
                break
        for idx,val in enumerate(list(zip(*grid))[::-1]):
            if 1 in list(val):
                maxy=(n-1)-idx
                break
        for i in range(m):
            if 1 in grid[i]:
                minx=i
                break
        for i in range(m-1,-1,-1):
            if 1 in grid[i]:
                maxx=i
                break

        result=(maxx-minx+1)*(maxy-miny+1)
        return result