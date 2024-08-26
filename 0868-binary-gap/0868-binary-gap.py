class Solution:
    def binaryGap(self, n: int) -> int:
        idx=[idx for idx,val in enumerate(bin(n)[2:]) if val=='1']
        result=0

        for i in range(len(idx)-1):
            result=max(result, idx[i+1]-idx[i])
        
        return result