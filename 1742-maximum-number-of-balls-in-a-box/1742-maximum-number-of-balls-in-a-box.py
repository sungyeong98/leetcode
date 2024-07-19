class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        num=Counter([sum(list(map(int,str(i)))) for i in range(lowLimit,highLimit+1)])
        return max(num.values())