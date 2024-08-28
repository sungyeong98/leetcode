class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result=''
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if all(s[k].swapcase() in s[i:j] for k in range(i,j)):
                    result=max(result,  s[i:j], key=len)
        return result