class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f,s,t=[],[],[]
        for i in firstWord:
            f.append(ord(i)-97)
        for i in secondWord:
            s.append(ord(i)-97)
        for i in targetWord:
            t.append(ord(i)-97)
        f=''.join(list(map(str,f)))
        s=''.join(list(map(str,s)))
        t=''.join(list(map(str,t)))
        if int(f)+int(s)==int(t):
            return True
        return False