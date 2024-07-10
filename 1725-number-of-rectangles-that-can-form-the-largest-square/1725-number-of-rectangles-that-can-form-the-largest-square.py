class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp=[min(i) for i in rectangles]
        return temp.count(max(temp))