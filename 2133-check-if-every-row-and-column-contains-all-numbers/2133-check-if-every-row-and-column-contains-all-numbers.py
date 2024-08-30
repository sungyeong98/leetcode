class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        target=set(range(1,n+1))
        for i in matrix:
            if set(i)!=target:
                return False
        for i in list(zip(*matrix)):
            if set(i)!=target:
                return False
        return True