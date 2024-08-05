class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result=[]
        for idx,(a,b) in enumerate(points):
            if x==a or y==b:
                result.append([abs(x-a)+abs(y-b),idx])
        if not result:
            return -1
        result.sort(key=lambda x:(x[0],x[1]))
        return result[0][1]