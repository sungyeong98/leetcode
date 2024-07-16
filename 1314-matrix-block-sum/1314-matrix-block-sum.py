class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            num=0

            for j in range(n):
                num+=mat[i][j]

                dp[i][j]=num

                if i>0:
                    dp[i][j]+=dp[i-1][j]

        result=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_r,max_r=max(0,i-k),min(m-1,i+k)
                min_c,max_c=max(0,j-k),min(n-1,j+k)

                result[i][j]=dp[max_r][max_c]

                if min_r>0:
                    result[i][j]-=dp[min_r-1][max_c]

                if min_c>0:
                    result[i][j]-=dp[max_r][min_c-1]
                
                if min_c>0 and min_r>0:
                    result[i][j]+=dp[min_r-1][min_c-1]
        return result