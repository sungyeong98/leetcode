class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=sorted(piles)
        alice,bob=0,0
        while n:
            alice+=n.pop()
            bob+=n.pop()
        return alice>bob