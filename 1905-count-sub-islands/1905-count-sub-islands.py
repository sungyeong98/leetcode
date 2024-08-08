class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=set()
        m,n=len(grid1),len(grid1[0])
        result=0

        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in visited:
                    temp=set()
                    temp.add((i,j))
                    stack=[(i,j)]

                    while stack:
                        x,y=stack.pop()

                        for dx,dy in dir:
                            nx=x+dx
                            ny=y+dy

                            if 0<=nx<m and 0<=ny<n and grid2[nx][ny]==1 and (nx,ny) not in temp:
                                temp.add((nx,ny))
                                stack.append((nx,ny))
                    
                    flag=True
                    for pos in temp:
                        x,y=pos
                        if grid1[x][y]!=1:
                            flag=False
                            break
                    
                    if flag:
                        result+=1
                    
                    visited.update(temp)
        return result