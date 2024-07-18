class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result=0
        box=deque(sorted(boxTypes,reverse=True, key=lambda x:x[1]))
        while box and truckSize>0:
            size,cnt=box.popleft()
            if truckSize>size:
                result+=(size*cnt)
                truckSize-=size
            else:
                result+=(cnt*truckSize)
                truckSize=0
        return result