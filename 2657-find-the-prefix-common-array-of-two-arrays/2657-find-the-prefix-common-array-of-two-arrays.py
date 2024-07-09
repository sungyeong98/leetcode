class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        result=[0]*n
        
        for i in range(n):
            a,b=A[:i+1],B[:i+1]
            result[i]=len(list(set(a)&set(b)))
        return result