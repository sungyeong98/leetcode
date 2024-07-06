class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):  return False
        for i, j in zip(words,list(s)):
            if i[0]!=j: return False
        return True