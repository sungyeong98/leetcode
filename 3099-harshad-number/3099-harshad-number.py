class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp=0
        for i in list(str(x)):
            temp+=int(i)
        if x%temp==0:   return temp
        return -1