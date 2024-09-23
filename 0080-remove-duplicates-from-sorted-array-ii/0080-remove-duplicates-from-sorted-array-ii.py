class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if result<2 or i!=nums[result-2]:
                nums[result]=i
                result+=1
        return result