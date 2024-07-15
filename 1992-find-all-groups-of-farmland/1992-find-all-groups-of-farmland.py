class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        m,n=len(land),len(land[0])
        result,visited=[],set()

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and land[i][j]==1:
                    stack=[(i,j)]
                    visited.add((i,j))
                    min_x,min_y=i,j
                    max_x,max_y=i,j

                    while stack:
                        x,y=stack.pop()
                        if x<min_x:     min_x=x
                        if x>max_x:     max_x=x
                        if y<min_y:     min_y=y
                        if y>max_y:     max_y=y

                        for dx,dy in dir:
                            nx=x+dx
                            ny=y+dy

                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and land[nx][ny]==1:
                                stack.append((nx,ny))
                                visited.add((nx,ny))
                    
                    result.append([min_x,min_y,max_x,max_y])
        return result