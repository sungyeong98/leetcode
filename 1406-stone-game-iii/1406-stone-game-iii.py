class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[0]*3

        for i in range(n-1,-1,-1):
            temp1=stoneValue[i]-dp[(i+1)%3]

            temp2=float('-inf')
            if i+1<n:
                temp2=stoneValue[i]+stoneValue[i+1]-dp[(i+2)%3]
            
            temp3=float('-inf')
            if i+2<n:
                temp3=stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[(i+3)%3]
            
            dp[i%3]=max(temp1,temp2,temp3)
        value=dp[0]
        if value>0:
            return 'Alice'
        elif value<0:
            return 'Bob'
        else:
            return 'Tie'