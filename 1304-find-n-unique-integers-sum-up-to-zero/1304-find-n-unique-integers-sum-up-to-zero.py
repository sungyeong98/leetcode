class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        temp=[i for i in range(1,n//2+1)]+[-i for i in range(1,n//2+1)]
        if n%2==1:
            return temp+[0]
        return temp