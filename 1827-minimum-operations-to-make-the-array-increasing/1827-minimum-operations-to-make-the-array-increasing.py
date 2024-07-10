class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                n=(nums[i]-nums[i+1])+1
                result+=n
                nums[i+1]+=n
        return result
            