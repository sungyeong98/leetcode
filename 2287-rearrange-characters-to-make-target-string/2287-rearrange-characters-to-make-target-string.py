class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c=Counter(s)
        t=Counter(target)
        result=[]
        for i in t:
            result.append(c[i]//t[i])
        return min(result)