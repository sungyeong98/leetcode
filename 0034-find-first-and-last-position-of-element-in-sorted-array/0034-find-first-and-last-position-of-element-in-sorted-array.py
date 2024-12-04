class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        start = nums.index(target)
        end = len(nums)-1

        if nums.count(target)==1:
            return [start, start]
        
        while nums[end]!=target:
            end-=1
        
        return [start, end]