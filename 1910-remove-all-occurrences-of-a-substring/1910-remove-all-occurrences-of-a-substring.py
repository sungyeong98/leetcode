class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(part)
        while part in s:
            target=s.find(part)
            s=s[:target]+s[target+n:]
        return s