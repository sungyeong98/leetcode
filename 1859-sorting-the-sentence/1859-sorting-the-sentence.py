class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(' ')
        n=len(s)
        result=[None]*n
        for i in s:
            result[int(i[-1])-1]=i[:-1]
        return ' '.join(result)