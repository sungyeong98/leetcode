class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        temp=list(set(word))
        temp.sort()
        result=0
        while temp:
            w=temp.pop()
            if w.islower() and w.upper() in temp:
                result+=1
                temp.pop(temp.index(w.upper()))
            elif w.isupper() and w.lower() in temp:
                result+=1
                temp.pop(temp.index(w.lower()))
        return result