class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result, temp = 0, x^y
        while temp:
            result+=temp&1
            result>>=1
        return result