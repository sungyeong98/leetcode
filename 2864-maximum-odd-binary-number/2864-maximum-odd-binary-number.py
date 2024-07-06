class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        cnt=list(s).count('1')
        result=''
        while len(result)<n:
            if cnt>1:
                result+='1'
                cnt-=1
            elif len(result)<n-1:
                result+='0'
            else:
                result+='1'
        return result