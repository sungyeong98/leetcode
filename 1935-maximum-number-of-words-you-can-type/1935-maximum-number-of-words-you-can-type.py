class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result=0
        for i in text.split(' '):
            if set(i)&set(brokenLetters):
                result+=1
        return result