class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        target=set("aeiouAEIOU")
        n=len(s)//2

        return True if sum(1 for i in s[:n] if i in target)==sum(1 for i in s[n:] if i in target) else False