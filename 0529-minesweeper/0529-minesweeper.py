class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        
        adjacent=lambda x,y: [(x+dx,y+dy) for dx in range(-1,2) for dy in range(-1,2) if (dx or dy) and 0<=x+dx<len(board) and 0<=y+dy<len(board[0])]

        def dfs(x,y):
            adj=adjacent(x,y)
            mines=sum(board[i][j]=='M' for i,j in adj)
            if mines:
                board[x][y]=str(mines)
            else:
                board[x][y]='B'
                for i,j in adj:
                    if board[i][j]=='E':
                        dfs(i,j)
            return 
        dfs(*click)
        return board