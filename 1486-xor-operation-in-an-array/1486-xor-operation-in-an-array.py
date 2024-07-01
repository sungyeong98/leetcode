class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[start+2*i for i in range(n)]
        result=start
        for i in range(1,n):
            result^=nums[i]
        return result