class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        result=set()
        for word in words:
            even=sorted(word[::2])
            odd=sorted(word[1::2])
            result.add((tuple(even), tuple(odd)))
        return len(result)