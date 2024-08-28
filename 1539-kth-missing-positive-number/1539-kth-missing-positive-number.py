class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        result=1
        while k>0:
            if result not in arr:
                k-=1
            result+=1
        return result