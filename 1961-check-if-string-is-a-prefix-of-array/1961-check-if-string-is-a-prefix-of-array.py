class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        if words[0]!=s[:len(words[0])]:
            return False
        n, idx = len(words), 1
        while idx<n+1:
            if s==''.join(words[:idx]):
                return True
            idx+=1
        return False
        