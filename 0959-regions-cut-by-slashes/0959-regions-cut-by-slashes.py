class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m,n=len(grid),len(grid[0])
        extend_grid=[[0]*(n*2) for _ in range(m*2)]

        for ori_x,new_x in zip(range(m), range(0,m*2,2)):
            for ori_y, new_y in zip(range(n), range(0,n*2,2)):
                if grid[ori_x][ori_y]=='/':
                    extend_grid[new_x][new_y+1]=1
                    extend_grid[new_x+1][new_y]=1
                elif grid[ori_x][ori_y]=='\\':
                    extend_grid[new_x][new_y]=1
                    extend_grid[new_x+1][new_y+1]=1

        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        result=0
        visited=set()
        for i in range(m*2):
            for j in range(n*2):
                if (i,j) not in visited and extend_grid[i][j]==0:
                    stack=[(i,j)]
                    visited.add((i,j))
                    while stack:
                        x,y=stack.pop()

                        for dx,dy in dir:
                            nx=x+dx
                            ny=y+dy

                            if 0<=nx<m*2 and 0<=ny<n*2 and (nx,ny) not in visited and extend_grid[nx][ny]==0:
                                visited.add((nx,ny))
                                stack.append((nx,ny))
                    result+=1
        return result