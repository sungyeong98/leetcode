class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result=len(text.split(' '))
        for i in text.split(' '):
            if set(i)&set(brokenLetters):
                result-=1
        return result