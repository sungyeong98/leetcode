class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:    return True
        for i in range(len(nums)-1):
            if nums[i]%2==0 and nums[i+1]%2==1:
                pass
            elif nums[i]%2==1 and nums[i+1]%2==0:
                pass
            else:
                return False
        return True