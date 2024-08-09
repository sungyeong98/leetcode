class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result=0
        m,n=len(grid),len(grid[0])
        if m<3 or n<3:
            return 0

        def isvalid(board):
            num=[j for i in board for j in i]
            if len(set(num))!=9:
                return False

            sum_val=0
            for i in board:
                if sum_val==0:
                    sum_val=sum(i)
                else:
                    if sum(i)!=sum_val:
                        return False
            
            for i in list(zip(*board)):
                if sum(i)!=sum_val:
                    return False
            
            left=board[0][0]+board[1][1]+board[2][2]
            right=board[0][2]+board[1][1]+board[2][0]
            if left!=sum_val or right!=sum_val:
                return False
            return True

        for i in range(m-2):
            for j in range(n-2):
                temp=[[grid[x][y] for y in range(j,j+3)] for x in range(i,i+3)]
                if isvalid(temp):
                    result+=1
        return result