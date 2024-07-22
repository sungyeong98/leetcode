class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        #solution1
        '''
        m,n=len(mat),len(mat[0])
        idx=[(i,j) for i in range(m) for j in range(n)]
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        target=[[0]*n for _ in range(m)]
        if target==mat: return 0
        result=[]

        def convert(board,position):
            x,y=position
            for dx,dy in dir:
                nx=x+dx
                ny=y+dy
                if 0<=nx<m and 0<=ny<n:
                    board[nx][ny]=1-board[nx][ny]
            board[x][y]=1-board[x][y]

        def dfs(board, visited, depth):
            if board==target:
                result.append(depth)
                return
            
            for x,y in idx:
                if (x,y) not in visited:
                    visited.add((x,y))
                    temp=[row[:] for row in board]
                    convert(temp,(x,y))
                    dfs(temp,visited,depth+1)
                    visited.remove((x,y))

        for position in idx:
            board=[row[:] for row in mat]
            visited=set()
            visited.add(position)
            convert(board,position)
            dfs(board, visited, 1)
        if not result:
            return -1
        return min(result)
        '''

        #solution2
        m,n=len(mat),len(mat[0])
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        target=[[0]*n for _ in range(m)]

        def convert(board,x,y):
            for dx,dy in dir:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    board[nx][ny]=1-board[nx][ny]
            board[x][y]=1-board[x][y]
        
        def mat_tuple(mat):
            return tuple(tuple(row) for row in mat)
        
        def bfs(start):
            queue=deque([(start,0)])
            visited=set()
            visited.add(mat_tuple(start))

            while queue:
                cur,depth=queue.popleft()

                if cur==target:
                    return depth
                
                for x in range(m):
                    for y in range(n):
                        new_board=[row[:] for row in cur]
                        convert(new_board,x,y)
                        new_state=mat_tuple(new_board)

                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_board,depth+1))
            return -1
        
        return bfs(mat)