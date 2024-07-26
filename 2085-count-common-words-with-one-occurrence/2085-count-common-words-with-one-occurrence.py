class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1=Counter(words1)
        w2=Counter(words2)
        result=0

        for w in list(set(words1+words2)):
            if w1[w]==1 and w2[w]==1:
                result+=1
        return result