class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        visited=set()

        for i in range(n):
            if grid[i][i]==0:
                return False
            if grid[i][n-i-1]==0:
                return False
            visited.add((i,i))
            visited.add((i,n-i-1))
        
        for i in range(n):
            for j in range(n):
                if (i,j) not in visited:
                    if grid[i][j]!=0:
                        return False
        
        return True