class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:    return False
        if len(list(set(sentence)))<26: return False
        else:   return True