class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        while nums:
            num=nums.pop(0)+nums.pop(-1)
            if num>result:
                result=num
        return result