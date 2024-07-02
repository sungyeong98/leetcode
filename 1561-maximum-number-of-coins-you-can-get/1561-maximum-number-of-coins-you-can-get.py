class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        piles.sort(reverse=True)
        piles=piles[:-n]

        result=0
        for i in range(1,len(piles),2):
            result+=piles[i]
        return result