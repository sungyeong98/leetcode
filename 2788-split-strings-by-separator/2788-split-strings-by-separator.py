class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [j for i in words for j in i.split(separator) if j]