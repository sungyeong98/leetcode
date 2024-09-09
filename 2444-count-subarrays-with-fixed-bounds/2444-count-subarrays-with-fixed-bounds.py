class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result=0
        bad_idx,left_idx,right_idx=-1,-1,-1
        for idx,num in enumerate(nums):
            if not minK<=num<=maxK:
                bad_idx=idx
            if num==minK:
                left_idx=idx
            if num==maxK:
                right_idx=idx
            result+=max(0,min(left_idx,right_idx)-bad_idx)
        return result