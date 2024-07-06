class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=0
        for i in range(len(arr)):
            for j in range(len(arr)+1):
                if len(arr[i:j])%2==1:
                    result+=sum(arr[i:j])
        return result