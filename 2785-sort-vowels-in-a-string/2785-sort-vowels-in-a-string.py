class Solution:
    def sortVowels(self, s: str) -> str:
        s=list(s)
        target=['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                if s[i] in target and s[j] in target:
                    if s[i]>s[j]:
                        s[i],s[j]=s[j],s[i]
        return ''.join(s)