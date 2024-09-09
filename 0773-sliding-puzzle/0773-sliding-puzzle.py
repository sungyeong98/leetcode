class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def get_nei(board):
            neighbors=[]
            r,c=0,0
            for i in range(2):
                for j in range(3):
                    if board[i][j]==0:
                        r,c=i,j
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc=r+i,c+j
                if 0<=nr<2 and 0<=nc<3:
                    new_board=[row[:] for row in board]
                    new_board[r][c]=new_board[nr][nc]
                    new_board[nr][nc]=0
                    neighbors.append(new_board)
            return neighbors
        
        queue=deque()
        queue.append((board,0))
        seen=set()
        seen.add(tuple(tuple(row) for row in board))

        while queue:
            board, moves=queue.popleft()
            if board ==[[1,2,3],[4,5,0]]:
                return moves
            for neighbor in get_nei(board):
                if tuple(tuple(row) for row in neighbor) not in seen:
                    queue.append((neighbor, moves+1))
                    seen.add(tuple(tuple(row) for row in neighbor))
        return -1