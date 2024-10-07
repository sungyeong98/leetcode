class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        num=int(s,2)
        while num>1:
            if num%2==0:
                num//=2
            else:
                num+=1
            result+=1
        return result