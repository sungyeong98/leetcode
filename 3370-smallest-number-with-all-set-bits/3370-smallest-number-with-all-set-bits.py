class Solution:
    def smallestNumber(self, n: int) -> int:
        result = '1'
        while True:
            if int(result,2)>=n:
                return int(result,2)
            result += '1'