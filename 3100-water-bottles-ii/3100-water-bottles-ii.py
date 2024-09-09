class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numBottles-=1
        d=(2*numExchange-3)**2 + 8*numBottles
        result=int((-(2*numExchange-3) + sqrt(d))/2)
        return numBottles+result+1