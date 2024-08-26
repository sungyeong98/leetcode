class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n<k:
            n,k=k,n
        if n&k!=k or n|k!=n:
            return -1
        
        result=0
        for i,j in zip_longest(bin(n)[2:][::-1], bin(k)[2:][::-1], fillvalue='0'):
            if i!=j:
                result+=1
        return result