class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        result=nums[0]
        for n1,n2 in pairwise(nums):
            if n2-n1==1:
                result+=n2
            else:
                break
        while result in nums:
            result+=1
        return result