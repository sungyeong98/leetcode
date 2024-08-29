class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        board=[[0]*(n+1) for _ in range(m+1)]
        for x,y in ops:
            board[0][0]+=1
            board[x][y]+=1
            board[0][y]-=1
            board[x][0]-=1

        for j in range(n):
            for i in range(1,m):
                board[i][j]+=board[i-1][j]

        for i in range(m):
            for j in range(1,n):
                board[i][j]+=board[i][j-1]
        
        temp=[board[i][j] for i in range(m) for j in range(n)]
        c=Counter(temp)
        return c[max(c.keys())]