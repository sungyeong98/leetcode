class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        target, start, end = m*n, 0, 0
        for i in range(m):
            target-=grid[i].count(-1)
            for j in range(n):
                if grid[i][j]==1:
                    start=(i,j)
                elif grid[i][j]==2:
                    end=(i,j)
        
        result, visited = [0], set()
        visited.add(start)

        def dfs(pos,visited):
            x,y=pos
            if (x,y) == end:
                if len(visited)==target:
                    result[0]+=1
                return
            
            for dx,dy in dir:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]!=-1:
                    visited.add((nx,ny))
                    dfs((nx,ny),visited)
                    visited.remove((nx,ny))
        
        dfs(start,visited)
        return result[0]