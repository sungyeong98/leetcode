class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result=0

        for i in grid:
            for j in list(zip(*grid)):
                if i==list(j):
                    result+=1

        return result