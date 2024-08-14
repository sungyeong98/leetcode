class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n=len(s)
        for i in range(n-1):
            temp=s[i:i+2][::-1]
            if temp in s:
                return True
        return False