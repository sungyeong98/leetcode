class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                grid[i][j]=cnt
                cnt+=1
        
        x,y=0,0
        for command in commands:
            if command=='DOWN':
                x+=1
            elif command=='UP':
                x-=1
            elif command=='LEFT':
                y-=1
            else:
                y+=1
        return grid[x][y]