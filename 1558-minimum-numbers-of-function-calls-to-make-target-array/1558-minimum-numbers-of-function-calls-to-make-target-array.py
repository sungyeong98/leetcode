class Solution:
    def minOperations(self, nums: List[int]) -> int:
        t, o = 0, 0
        for num in nums:
            mul=0
            while num:
                if num%2:
                    num-=1
                    o+=1
                else:
                    num//=2
                    mul+=1
            t=max(t,mul)
        return o+t