class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        m,n=len(grid),len(grid[0])
        result=0

        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    stack=[(i,j)]
                    cnt=1
                    while stack:
                        x,y=stack.pop()

                        for dx,dy in dir:
                            nx=x+dx
                            ny=y+dy
                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]==1:
                                visited.add((nx,ny))
                                stack.append((nx,ny))
                                cnt+=1
                    if cnt>result:
                        result=cnt
        return result