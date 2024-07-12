class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*n

        for i in range(n):
            cur_max=0
            for j in range(1,min(k,i+1)+1):
                cur_max=max(cur_max, arr[i-j+1])

                if i-j>=0:
                    dp[i]=max(dp[i], dp[i-j]+cur_max*j)
                else:
                    dp[i]=max(dp[i], cur_max*j)
        return dp[-1]