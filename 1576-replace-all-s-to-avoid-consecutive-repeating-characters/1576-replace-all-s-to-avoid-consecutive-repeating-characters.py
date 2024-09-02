class Solution:
    def modifyString(self, s: str) -> str:
        s=list(s)
        n=len(s)
        for i in range(n):
            if s[i]=='?':
                for j in 'abc':
                    if (i==0 or s[i-1]!=j) and (i+1==n or s[i+1]!=j):
                        s[i]=j
                        break
        return ''.join(s)