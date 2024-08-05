class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result=0
        for i in range(len(arr)-k+1):
            if sum(arr[i:i+k])>=threshold*k:
                result+=1
        return result