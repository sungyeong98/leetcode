class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3: return False
        for i in '@#$':
            if i in word:
                return False
        v,d,a=False,False,False
        for i in 'aeiou':
            if i in word or i.upper() in word:
                v=True
                break
        for i in range(0,10):
            if str(i) in word:
                d=True
                break
        for i in range(ord('a'),ord('z')+1):
            if chr(i) in word or chr(i).upper() in word:
                a=True
                break
        return v&d or v&d&a