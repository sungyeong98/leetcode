class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        result=[0]*(n+1)
        for i in range(1,n+1):
            if i==1:
                result[i]=1
            elif i%2==0:
                result[i]=result[i//2]
            else:
                result[i]=result[i//2]+result[i//2+1]
        return max(result)