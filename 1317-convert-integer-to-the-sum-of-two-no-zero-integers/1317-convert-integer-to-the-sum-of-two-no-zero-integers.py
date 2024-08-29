class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isvalid(num):
            while num>0:
                if num%10==0:
                    return False
                num//=10
            return True
        
        for i in range(1,n):
            temp=n-i
            if isvalid(temp) and isvalid(i):
                return [i,temp]