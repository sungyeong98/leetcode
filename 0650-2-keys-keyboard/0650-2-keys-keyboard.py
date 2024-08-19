class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        
        step, fac = 0, 2
        while n>1:
            while n%fac==0:
                step+=fac
                n//=fac
            fac+=1
        
        return step