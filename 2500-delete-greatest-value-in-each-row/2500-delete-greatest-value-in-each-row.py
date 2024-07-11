class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        temp=[sorted(i,reverse=True) for i in grid]
        result=0
        for i in list(zip(*temp)):
            result+=max(i)
        return result