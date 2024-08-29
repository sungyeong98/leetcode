class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        n=len(mat)
        def rotate_90(mat):
            temp=[[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    temp[j][n-1-i]=mat[i][j]
            return temp
        def rotate_180(mat):
            temp=[[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    temp[n-1-i][n-1-j]=mat[i][j]
            return temp
        def rotate_270(mat):
            temp=[[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    temp[n-1-j][i]=mat[i][j]
            return temp
        
        t1,t2,t3=rotate_90(mat),rotate_180(mat),rotate_270(mat)
        return True if target==t1 or target==t2 or target==t3 else False