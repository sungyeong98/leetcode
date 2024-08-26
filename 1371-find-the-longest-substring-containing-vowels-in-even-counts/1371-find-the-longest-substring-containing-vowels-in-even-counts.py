class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel={'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        d,n,result={0:-1},0,0
        for idx,c in enumerate(s):
            if c in vowel:
                n^=vowel[c]
            if n not in d:
                d[n]=idx
            else:
                result=max(result, idx-d[n])
        return result