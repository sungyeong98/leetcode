class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        while nums:
            result.append(nums.pop())
            if sum(result)>sum(nums):
                break
        return result