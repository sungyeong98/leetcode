class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f,s,t=[],[],[]
        for i in firstWord:
            f.append(ord(i)-97)
        for i in secondWord:
            s.append(ord(i)-97)
        for i in targetWord:
            t.append(ord(i)-97)
        if sum(f)+sum(s)==sum(t):
            return True
        return False