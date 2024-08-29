class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)[::-1]
        result='.'.join(s[i:i+3] for i in range(0,len(s),3))
        return result[::-1]