class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        result=0

        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i,j) not in visited:
                    visited.add((i,j))
                    stack=[(i,j)]
                    flag=True

                    while stack:
                        x,y=stack.pop()

                        for dx,dy in dir:
                            nx,ny=x+dx,y+dy

                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]==0:
                                visited.add((nx,ny))
                                stack.append((nx,ny))

                            elif nx<0 or nx>=m or ny<0 or ny>=n:
                                flag=False
                    
                    if flag:
                        result+=1
        return result