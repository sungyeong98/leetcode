class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        c=set(chars)
        for word in words:
            n=len(word)
            if len(set(word)-c)==0:
                result+=n
        return result