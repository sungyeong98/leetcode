class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s=sentence.split(' ')
        s=s+[s[0]]
        prev=None
        for i in s:
            if prev!=None and prev!=i[0]:
                return False
            prev=i[-1]
        return True