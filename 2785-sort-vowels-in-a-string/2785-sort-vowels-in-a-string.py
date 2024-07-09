class Solution:
    def sortVowels(self, s: str) -> str:
        s=list(s)
        target=['a','e','i','o','u','A','E','I','O','U']
        temp, pos = [], []
        for i in range(len(s)):
            if s[i] in target:
                pos.append(i)
                temp.append(s[i])
        temp.sort()
        temp=iter(temp)
        for i in pos:
            s[i]=next(temp)
        return ''.join(s)