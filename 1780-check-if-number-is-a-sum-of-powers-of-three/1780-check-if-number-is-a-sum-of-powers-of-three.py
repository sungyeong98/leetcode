class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        temp=''
        while n>0:
            temp=str(n%3)+temp
            n//=3
        return '2' not in temp