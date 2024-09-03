class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        temp=None
        for i in range(n-1):
            x1,y1=coordinates[i]
            x2,y2=coordinates[i+1]
            if temp is None:
                temp=abs(y2-y1)/abs(x2-x1)
            elif temp!=abs(y2-y1)/abs(x2-x1):
                return False
        return True