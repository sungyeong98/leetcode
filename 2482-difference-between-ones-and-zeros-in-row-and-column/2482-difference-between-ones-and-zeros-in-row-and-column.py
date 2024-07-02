class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        rev_grid=list(map(list,zip(*grid)))

        row=[sum(grid[i])-(m-sum(grid[i])) for i in range(m)]
        col=[sum(rev_grid[i])-(n-sum(rev_grid[i])) for i in range(n)]

        result=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j]=row[i]+col[j]

        return result