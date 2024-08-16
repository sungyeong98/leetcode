class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        left, right = arrays[0][0], arrays[0][-1]
        result=0

        for i in range(1, len(arrays)):
            arr=arrays[i]
            result=max(result, abs(arr[-1]-left), abs(right-arr[0]))
            left=min(left, arr[0])
            right=max(right, arr[-1])
        
        return result