class Solution:
    def repeatedCharacter(self, s: str) -> str:
        temp=set()
        for i in s:
            if i not in temp:
                temp.add(i)
            else:
                return i