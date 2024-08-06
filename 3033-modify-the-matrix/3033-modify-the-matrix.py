class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        col_max={}
        for idx, seq in enumerate(list(zip(*matrix))):
            col_max[idx]=max(seq)

        result=[[matrix[i][j] if matrix[i][j]!=-1 else col_max[j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        return result