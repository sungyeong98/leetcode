class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1=Counter(word1)
        w2=Counter(word2)
        w=set(word1+word2)
        for i in w:
            if i in w1 and i in w2:
                if abs(w1[i]-w2[i])>3:
                    return False
            elif i in w1:
                if w1[i]>3:
                    return False
            elif i in w2:
                if w2[i]>3:
                    return False
        return True