class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp=[i for i in nums if i>=k]
        return len(nums)-len(temp)