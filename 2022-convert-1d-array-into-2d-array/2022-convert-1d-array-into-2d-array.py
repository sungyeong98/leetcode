class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=(m*n):
            return []
        result=[[0]*n for _ in range(m)]
        o=iter(original)
        for i in range(m):
            for j in range(n):
                result[i][j]=next(o)
        return result