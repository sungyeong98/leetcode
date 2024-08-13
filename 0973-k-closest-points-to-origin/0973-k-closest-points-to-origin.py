class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp={}
        for idx,(x,y) in enumerate(points):
            n=math.sqrt(x**2+y**2)
            temp[idx]=n

        temp=dict(sorted(temp.items(), key=lambda x:x[1]))
        result=[]
        for i in temp:
            result.append(points[i])
            if len(result)==k:
                break
        return result