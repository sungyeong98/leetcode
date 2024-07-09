class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        result, n = '', len(s)
        if n<=1:
            return s

        for i, j in zip(s, s[::-1]):
            result+=min(i,j)
            if len(result)==n//2:
                break
        if n%2==1:
            return result+s[n//2]+result[::-1]
        return result+result[::-1]