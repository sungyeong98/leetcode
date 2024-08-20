class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if not piles:
            return 0
        n=len(piles)
        dp=[[0]*n for _ in range(n)]
        suffix=[0]*n
        suffix[-1]=piles[-1]

        for i in range(n-2,-1,-1):
            suffix[i]=piles[i]+suffix[i+1]
        
        def helper(i, m):
            if i==n:
                return 0
            if i+2*m>=n:
                return suffix[i]
            if dp[i][m]!=0:
                return dp[i][m]
            
            result=0
            for x in range(1,2*m+1):
                result=max(result, suffix[i]-helper(i+x,max(m,x)))
            dp[i][m]=result

            return result
        return helper(0,1)