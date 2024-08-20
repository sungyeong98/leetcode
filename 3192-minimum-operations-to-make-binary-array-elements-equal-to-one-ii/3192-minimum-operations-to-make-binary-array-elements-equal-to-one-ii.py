class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            if i==result%2:
                result+=1
        return result