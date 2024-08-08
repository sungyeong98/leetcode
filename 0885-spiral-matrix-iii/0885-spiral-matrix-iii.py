class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result=[]
        visited=[[False]*cols for _ in range(rows)]
        dir=[(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx=0
        r,c=rStart,cStart
        step=1

        result.append([r,c])
        visited[r][c]=True

        while len(result)<rows*cols:
            for _ in range(2):
                for _ in range(step):
                    r+=dir[dir_idx][0]
                    c+=dir[dir_idx][1]

                    if 0<=r<rows and 0<=c<cols and not visited[r][c]:
                        result.append([r,c])
                        visited[r][c]=True
                    if len(result)==rows*cols:
                        return result
                    
                dir_idx=(dir_idx+1)%4
            step+=1

        return result