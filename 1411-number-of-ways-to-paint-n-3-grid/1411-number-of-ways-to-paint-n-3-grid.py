class Solution:
    def numOfWays(self, n: int) -> int:
        x, y, mod = 0, 3, 10**9+7
        for _ in range(n):
            x, y = (3*x+2*y)%mod, (2*x+2*y)%mod
        return (x+y)%mod