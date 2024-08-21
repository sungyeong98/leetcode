class Solution:
    def countOrders(self, n: int) -> int:
        mod=(10**9)+7

        dp=[0]*(n+1)
        dp[0]=1

        for i in range(1,n+1):
            dp[i]=dp[i-1]*(2*i-1)*i%mod
        return dp[-1]