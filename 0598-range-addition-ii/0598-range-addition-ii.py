class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_r, min_c = m, n
        for i in range(len(ops)):
            min_r=min(min_r, ops[i][0])
            min_c=min(min_c, ops[i][1])
        return min_r*min_c