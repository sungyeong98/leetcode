class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp=sorted([(val,idx) for idx,val in enumerate(nums)])
        return [val for val,idx in sorted(temp[-k:],key=lambda x:x[1])]