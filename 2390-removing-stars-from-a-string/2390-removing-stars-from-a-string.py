class Solution:
    def removeStars(self, s: str) -> str:
        while '*' in s:
            idx=s.index('*')
            
            s=s.replace(s[idx-1:idx+1],'')
        return s