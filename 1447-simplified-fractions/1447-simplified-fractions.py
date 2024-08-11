class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result=[]
        if n==1:    return result
        for i in range(2,n+1):
            temp='/'+str(i)
            for j in range(1,i):
                if (i%j)%2==1 or j==1:
                    result.append(str(j)+temp)
        return result