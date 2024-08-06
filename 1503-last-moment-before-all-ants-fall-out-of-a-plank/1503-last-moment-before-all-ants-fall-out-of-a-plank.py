class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        result=0
        for i in left:
            result=max(result, i)
        for i in right:
            result=max(result, n-i)
        return result