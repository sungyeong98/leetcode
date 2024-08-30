class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        if y<4: return 'Bob'
        return 'Alice' if min(x//2,y//8)%2==0 else 'Bob'