class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp_asc=sorted(nums)
        temp_desc=sorted(nums,reverse=True)
        return True if nums==temp_asc or nums==temp_desc else False