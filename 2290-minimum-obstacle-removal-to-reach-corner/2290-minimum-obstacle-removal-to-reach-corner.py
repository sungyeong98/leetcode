class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dis = [[float('inf') for _ in range(n)] for _ in range(m)]
        temp = deque()

        dis[0][0]=0
        temp.appendleft((0,0))
        dir=[(0,1),(1,0),(0,-1),(-1,0)]

        while temp:
            x,y=temp.popleft()

            for dx,dy in dir:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    next_dis = dis[x][y] + grid[nx][ny]
                    if next_dis<dis[nx][ny]:
                        dis[nx][ny]=next_dis

                        if grid[nx][ny]==0:
                            temp.appendleft((nx,ny))
                        else:
                            temp.append((nx,ny))

        return dis[m-1][n-1]