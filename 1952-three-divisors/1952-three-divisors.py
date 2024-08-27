class Solution:
    def isThree(self, n: int) -> bool:
        if n==1:    return False
         
        temp=int(sqrt(n))
        if temp*temp!=n:
            return False
        for i in range(2,int(sqrt(temp))+1):
            if temp%i==0:
                return False
        return True