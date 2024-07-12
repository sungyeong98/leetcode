class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        #solution1
        '''
        r,c=len(rowSum),len(colSum)
        result=[[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                rsum,csum=rowSum[i], colSum[j]
                min_num=min(rsum,csum)
                result[i][j]=min_num
                rowSum[i]-=min_num
                colSum[j]-=min_num
        return result
        '''

        #solution2
        col_sum = colSum
        row_sum = rowSum
        
        mat = [[0]*len(col_sum) for i in range(len(row_sum))]
        i = 0
        j = 0
        while i < len(row_sum) and j < len(col_sum):
            mat[i][j] = min(row_sum[i], col_sum[j])
            if row_sum[i] == col_sum[j]:
                i += 1
                j += 1
            elif row_sum[i] > col_sum[j]:
                row_sum[i] -= col_sum[j]
                j += 1
            else:
                col_sum[j] -= row_sum[i]
                i += 1

        return mat