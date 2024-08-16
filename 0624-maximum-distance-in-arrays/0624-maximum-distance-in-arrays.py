class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
        left,right=0,0
        if abs(arrays[0][0])>abs(arrays[0][-1]):
            left=arrays[0][-1]
        else:
            left=arrays[0][0]
        
        return abs(arrays[-1][-1]-left)