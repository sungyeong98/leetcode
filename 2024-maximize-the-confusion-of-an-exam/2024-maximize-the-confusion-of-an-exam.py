class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def count(c,k):
            lo,win=-1,0
            for hi in range(len(answerKey)):
                k-=answerKey[hi]==c
                while k<0:
                    lo+=1
                    k+=answerKey[lo]==c
                win=max(win,hi-lo)
            return win
        return max(count('T',k), count('F',k))