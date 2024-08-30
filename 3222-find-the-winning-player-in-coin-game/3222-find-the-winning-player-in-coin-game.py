class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        temp=min(x,y//4)
        return 'Alice' if temp%2 else 'Bob'