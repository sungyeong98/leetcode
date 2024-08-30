class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        if words[startIndex]==target:
            return 0
        for i in range(len(words)):
            if words[(startIndex+i)%len(words)]==target or words[(startIndex-i)%len(words)]==target:
                return i