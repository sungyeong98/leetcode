class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result=0
        while n:
            result=-result-(n^(n-1))
            n&=n-1
        return abs(result)