class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n=len(matrix),len(matrix[0])
        idx=[]
        for i in range(m):
            idx.append((i,0))
        for i in range(n):
            idx.append((0,i))
        idx.pop(0)

        for pos in idx:
            x,y=pos
            num=matrix[x][y]
            while 0<=x+1<m and 0<=y+1<n:
                x+=1
                y+=1
                if matrix[x][y]!=num:
                    return False
        return True