class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result=0
        n=sum(arr[0:k])
        if n>=threshold*k:
            result+=1

        for i in range(1,len(arr)-k+1):
            n-=arr[i-1]
            n+=arr[i+k-1]
            if n>=threshold*k:
                result+=1
        return result