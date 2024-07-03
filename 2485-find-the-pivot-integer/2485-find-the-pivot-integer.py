class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1: return 1
        temp=[i for i in range(1,n+1)]

        for i in range(n):
            if sum(temp[:i+1])==sum(temp[i:]):
                return i+1
        
        return -1