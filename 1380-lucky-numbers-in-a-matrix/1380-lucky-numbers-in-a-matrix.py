class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for row in matrix:
            for col in list(zip(*matrix)):
                if min(row)==max(col):
                    return [min(row)]
            