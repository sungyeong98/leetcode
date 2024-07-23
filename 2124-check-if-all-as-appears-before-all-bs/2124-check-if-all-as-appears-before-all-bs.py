class Solution:
    def checkString(self, s: str) -> bool:
        a=list(filter(lambda x:s[x]=='a', range(len(s))))
        b=list(filter(lambda x:s[x]=='b', range(len(s))))
        if a and b and max(a)>min(b):
            return False
        return True