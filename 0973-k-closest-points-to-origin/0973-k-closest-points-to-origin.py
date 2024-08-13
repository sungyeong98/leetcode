class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp={}
        for x,y in points:
            n=math.sqrt(x**2+y**2)
            temp[(x,y)]=n

        temp=dict(sorted(temp.items(), key=lambda x:x[1]))
        result=[i for i in temp.keys()]

        return result[:k]