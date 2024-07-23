class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        temp={(i,j):abs(i-rCenter)+abs(j-cCenter) for i in range(rows) for j in range(cols)}
        result=list(sorted(temp.keys(), key=lambda x:temp[x]))
        return result