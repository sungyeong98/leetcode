class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        result=0
        n=len(arr)
        if arr[0]!=1:
            arr[0]=1
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])<=1:
                continue
            else:
                arr[i+1]=arr[i]+1
        return max(arr)