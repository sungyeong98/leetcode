class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result=float('inf')
        idx=[i for i in range(len(nums)) if nums[i]==target]
        for i in idx:
            result=min(result,abs(start-i))
        return result