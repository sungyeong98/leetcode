class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        
        cnt, temp = 0, 10
        while n>=temp:
            n-=temp
            temp-=1
            cnt+=1
        return cnt%2!=0