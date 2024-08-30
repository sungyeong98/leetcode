class Solution:
    def check(self, nums: List[int]) -> bool:
        target=sorted(nums)
        n=len(nums)
        cnt=0
        while cnt<n:
            nums=nums[1:]+nums[:1]
            if nums==target:
                return True
            cnt+=1
        return False