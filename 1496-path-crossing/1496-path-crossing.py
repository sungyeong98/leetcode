class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir={'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}
        pos=(0,0)
        visited=set()
        visited.add(pos)
        for i in path:
            x,y=pos
            nx=x+dir[i][0]
            ny=y+dir[i][1]
            if (nx,ny) not in visited:
                visited.add((nx,ny))
            else:
                return True
            pos=(nx,ny)
        return False