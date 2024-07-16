class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        result,m,n=0,len(board),len(board[0])
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=set()

        for i in range(m):
            for j in range(n):
                if board[i][j]!='.' and (i,j) not in visited:
                    stack=[(i,j)]
                    visited.add((i,j))
                    while stack:
                        x,y=stack.pop()
                        for dx,dy in dir:
                            nx=x+dx
                            ny=y+dy
                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and board[nx][ny]!='.':
                                visited.add((nx,ny))
                                stack.append((nx,ny))
                    result+=1
        return result