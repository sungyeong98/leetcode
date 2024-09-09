class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        result=''
        n1,n2,n3=str(num1)[::-1], str(num2)[::-1], str(num3)[::-1]
        for i,j,k in zip_longest(n1,n2,n3, fillvalue='0'):
            temp=min(int(i),int(j),int(k))
            result+=str(temp)
        return int(result[::-1])