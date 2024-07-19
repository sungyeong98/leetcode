class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result=[0,0]
        while n>0:
            if n%2==1:
                if (n//2)%2==0:
                    result[1]+=1
                else:
                    result[0]+=1
            n//=2
        return result