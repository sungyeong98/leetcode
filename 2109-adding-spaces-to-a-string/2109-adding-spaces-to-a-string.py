class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ''
        for idx, word in enumerate(s):
            if idx in spaces:
                result+=' '
            result+=word
        return result