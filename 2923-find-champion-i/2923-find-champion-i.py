class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        result=[0,0]
        for idx,val in enumerate(grid):
            if sum(val)>result[1]:
                result=[idx,sum(val)]
        return result[0]