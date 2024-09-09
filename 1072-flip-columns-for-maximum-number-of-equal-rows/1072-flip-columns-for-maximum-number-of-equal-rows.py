class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        temp=defaultdict(int)
        for row in matrix:
            temp[tuple(row)]+=1
            flip=[1-c for c in row]
            temp[tuple(flip)]+=1
        return max(temp.values())