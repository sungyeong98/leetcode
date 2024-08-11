class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1:    return []

        result=[]
        for i in range(2,n+1):
            temp='/'+str(i)
            for j in range(1,i):
                flag=True
                if j>1:
                    for k in range(1,j+1):
                        if k!=1 and (j%k==0 and i%k==0):
                            flag=False
                            break
                if flag:
                    result.append(str(j)+temp)
        return result