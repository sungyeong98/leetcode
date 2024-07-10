class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return len(list(set(nums)))