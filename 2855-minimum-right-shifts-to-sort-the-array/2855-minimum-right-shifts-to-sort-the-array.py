class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        result=0
        target=sorted(nums)
        if target==nums:
            return 0

        while nums!=target:
            nums=nums[-1:]+nums[:-1]
            result+=1
            if result>=len(nums):
                return -1
        return result