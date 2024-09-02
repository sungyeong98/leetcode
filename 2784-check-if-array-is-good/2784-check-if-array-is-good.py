class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        if max(nums)+1!=n:
            return False
        if nums.count(max(nums))!=2:
            return False
        temp=list(range(1,n))
        if temp!=nums[:-1]:
            return False
        return True