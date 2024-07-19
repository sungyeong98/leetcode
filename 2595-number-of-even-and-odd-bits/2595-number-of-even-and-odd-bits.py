class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result=[0,0]
        flag=True
        while n>0:
            if n%2==1:
                if flag:
                    result[0]+=1
                else:
                    result[1]+=1
            if flag:
                flag=False
            else:
                flag=True
            n//=2
        return result