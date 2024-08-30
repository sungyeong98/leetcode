class Solution:
    def countOdds(self, low: int, high: int) -> int:
        temp=(high-low)//2
        if low%2==1 or high%2==1:
            temp+=1
        return temp