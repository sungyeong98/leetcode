class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(pref)
        result=0
        for i in words:
            if i[:n]==pref:
                result+=1
        return result