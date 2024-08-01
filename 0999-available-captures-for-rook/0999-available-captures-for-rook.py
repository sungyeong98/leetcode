class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R=None
        for i in range(8):
            if 'R' not in board[i]:
                continue
            for j in range(8):
                if board[i][j]=='R':
                    R=(i,j)
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        pos=0
        result=0
        while pos<4:
            cx,cy=R
            dx,dy=dir[pos]
            while 0<=cx+dx<8 and 0<=cy+dy<8:
                cx+=dx
                cy+=dy
                
                if board[cx][cy]=='.':
                    continue
                elif board[cx][cy]=='p':
                    result+=1
                    break
                else:
                    break
            pos+=1
        return result