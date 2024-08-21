class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                map[i][j]=max(map[i][j], map[i-1][j]+map[i][j-1])
        return map[m-1][n-1]