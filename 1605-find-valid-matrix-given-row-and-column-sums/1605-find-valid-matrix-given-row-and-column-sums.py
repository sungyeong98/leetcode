class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
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