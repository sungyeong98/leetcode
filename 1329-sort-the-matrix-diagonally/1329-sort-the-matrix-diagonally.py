class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        temp=[]
        m,n=len(mat),len(mat[0])

        for i in range(m):
            temp.append([i,0])
        for i in range(n):
            temp.append([0,i])
        temp.pop(0)
        
        for x,y in temp:
            arr=[]
            nx,ny=x,y

            while nx<m and ny<n:
                arr.append(mat[nx][ny])
                nx,ny=nx+1,ny+1
            arr.sort()
            
            nx,ny=x,y
            while nx<m and ny<n:
                mat[nx][ny]=arr.pop(0)
                nx,ny=nx+1,ny+1
        return mat
        '''
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
        '''