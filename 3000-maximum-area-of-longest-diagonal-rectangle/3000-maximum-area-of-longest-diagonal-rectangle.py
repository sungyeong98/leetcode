class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        temp=sorted([(x*x+y*y,x*y) for x,y in dimensions], key=lambda x:(-x[0],-x[1]))
        return temp[0][1]