class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        target=list(allowed)
        result=0
        for word in words:
            flag=True
            for w in list(word):
                if w not in target:
                    flag=False
                    break
            if flag:
                result+=1
        return result