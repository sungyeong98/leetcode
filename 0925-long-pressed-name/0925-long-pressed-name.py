class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        c1=Counter(name)
        c2=Counter(typed)
        s=set(name+typed)
        for i in s:
            if i not in c1:
                return False
            if c1[i]>c2[i]:
                return False
        return True