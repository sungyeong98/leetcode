class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles=deque(piles)
        alice=[]
        bob=[]

        while piles:
            if piles[-1]>piles[0]:
                alice.append(piles.pop())
            elif piles[0]>piles[-1]:
                alice.append(piles.popleft())
            else:
                alice.append(piles.pop())

            if piles[-1]>piles[0]:
                bob.append(piles.pop())
            elif piles[0]>piles[-1]:
                bob.append(piles.popleft())
            else:
                bob.append(piles.pop())
        
        return sum(alice)>sum(bob)