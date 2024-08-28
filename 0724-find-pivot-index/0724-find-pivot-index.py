class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        prev=None

        for idx,val in enumerate(nums):
            if prev is None:
                prev=val
                right-=val
            else:
                left+=prev
                right-=val
                prev=val
            if left==right:
                return idx
        return -1