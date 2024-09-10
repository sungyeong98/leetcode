class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect(nums,target)-1 if target in nums else -1