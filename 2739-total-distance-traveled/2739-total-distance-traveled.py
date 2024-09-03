class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result,i=0,0
        while i<mainTank:
            i+=1
            if additionalTank!=0 and i%5==0:
                additionalTank-=1
                result+=10
                mainTank+=1
            else:
                result+=10
        return result