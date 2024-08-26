class Solution:
    def minChanges(self, n: int, k: int) -> int:
        k^=n
        cnt=bin(k).count('1')
        k&=n
        return cnt if cnt==bin(k).count('1') else -1