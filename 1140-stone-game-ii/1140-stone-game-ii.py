class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        prefix_sum=[0]*(n+1)

        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+piles[i]

        dp=[[0]*(n+1) for _ in range(n+1)]

        def dfs(idx,m):
            if idx>=n:
                return 0
            if dp[idx][m]>0:
                return dp[idx][m]
            
            max_stone=0
            for i in range(1,min(2*m, n-idx)+1):
                stones=prefix_sum[idx+i]-prefix_sum[idx]

                max_stone=max(max_stone, stones-dfs(idx+i, max(m, i)))

            dp[idx][m]=max_stone
            return max_stone
        return dfs(0,1)