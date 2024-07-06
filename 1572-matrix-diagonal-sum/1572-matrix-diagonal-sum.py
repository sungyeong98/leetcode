class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        temp=set()
        for i in range(n):
            temp.add((i,i))
            temp.add((i,n-1-i))
        return sum([mat[i][j] for i,j in temp])