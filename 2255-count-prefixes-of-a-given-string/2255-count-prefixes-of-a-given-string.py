class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        result=0
        for word in words:
            if len(word)<=len(s) and word==s[:len(word)]:
                result+=1
        return result