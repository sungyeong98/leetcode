class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n, f = len(encoded)+1, 0
        for i in range(1,n+1):
            f^=i
        for i in range(1,n,2):
            f^=encoded[i]
        perm=[0]*n
        perm[0]=f
        for i in range(n-1):
            perm[i+1]=perm[i]^encoded[i]
        return perm