class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result=0
        m,n=len(grid),len(grid[0])
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    stack=[(i,j)]
                    visited.add((i,j))
                    cnt=1
                    flag=False
                    while stack:
                        x,y=stack.pop()
                        for dx,dy in dir:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]==1:
                                cnt+=1
                                stack.append((nx,ny))
                                visited.add((nx,ny))
                            elif nx<0 or nx>=m or ny<0 or ny>=n:
                                flag=True
                    if not flag:
                        result+=cnt
        return result