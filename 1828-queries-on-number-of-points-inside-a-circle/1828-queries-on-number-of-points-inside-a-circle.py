class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result=[]
        for x,y,r in queries:
            cnt=0
            for i,j in points:
                if abs(x-i)**2+abs(y-j)**2<=r**2:
                    cnt+=1
            result.append(cnt)
        return result