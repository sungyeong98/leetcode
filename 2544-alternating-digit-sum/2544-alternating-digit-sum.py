class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result=0
        for idx,val in enumerate(list(str(n))):
            if idx%2==0:
                result+=int(val)
            else:
                result-=int(val)
        return result