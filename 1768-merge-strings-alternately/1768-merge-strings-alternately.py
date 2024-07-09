class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''
        w1,w2=list(word1),list(word2)
        while w1 or w2:
            if w1:
                result+=w1.pop(0)
            if w2:
                result+=w2.pop(0)
        return result