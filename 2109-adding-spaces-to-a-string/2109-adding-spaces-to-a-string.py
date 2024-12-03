class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=list(s)
        for i in spaces:
            result[i]=' '+result[i]
        return ''.join(result)