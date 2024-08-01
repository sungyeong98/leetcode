class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        def isvalid(board,row,col):
            for r,c in enumerate(board):
                if col==c or abs(row-r)==abs(col-c):
                    return False
            return True
        def backtrack(level,board,visited):
            if level==n:
                result.append(['.'*i+'Q'+'.'*(n-i-1) for i in board])
                return
            
            for i in range(n):
                if i not in visited and isvalid(board,level,i):
                    board.append(i)
                    visited.add(i)
                    backtrack(level+1, board, visited)
                    board.pop()
                    visited.remove(i)
        backtrack(0,[],set())
        return result