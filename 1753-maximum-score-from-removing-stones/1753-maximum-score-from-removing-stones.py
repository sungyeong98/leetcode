class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles=sorted([a,b,c])
        a,b,c=piles[0],piles[1],piles[2]

        max_score=min((a+b+c)//2, a+b)
        return max_score