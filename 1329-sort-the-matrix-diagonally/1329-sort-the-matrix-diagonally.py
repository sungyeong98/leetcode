class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                nx,ny=i+1,j+1
                while nx<m and ny<n:
                    if mat[i][j]>mat[nx][ny]:
                        mat[i][j],mat[nx][ny]=mat[nx][ny],mat[i][j]
                    nx+=1
                    ny+=1
        return mat